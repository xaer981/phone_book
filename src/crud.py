import csv
import logging
import os
from itertools import islice
from operator import attrgetter
from pathlib import Path

from colorama import Fore
from prettytable import PrettyTable, from_csv
from pydantic import BaseModel

from src import constants
from src.schemas import Contact


class BookCrud:
    def __init__(self, book_path: Path, model: BaseModel) -> None:
        self.phone_book = book_path.with_suffix('.csv')
        self.model = model

    def get_all(self) -> PrettyTable:
        """
        Получает весь список контактов.
        В случае пустой таблицы - печатает сообщение и закрывается.

        Returns:
            PrettyTable: таблица с контактами.
        """
        contact_titles = map(attrgetter('title'),
                             self.model.model_fields.values())
        logging.info('Получаю список контактов.')
        try:
            with open(self.phone_book,
                      mode='r',
                      encoding=constants.DEFAULT_ENCODING) as file:
                table = from_csv(file, field_names=contact_titles)
                table.add_autoindex('ID')

        except csv.Error:
            print(Fore.RED + constants.PHONE_BOOK_EMPTY_MESSAGE)
            logging.error(constants.PHONE_BOOK_EMPTY_MESSAGE)
            exit(1)

        return table

    def add(self, instance: BaseModel) -> None:
        """
        Добавляет контакт в конец таблицы.

        Args:
            instance (BaseModel): контакт, добавляемый в таблицу.
        """
        logging.info(f'Добавляю контакт {instance}')
        with open(self.phone_book,
                  mode='a',
                  encoding=constants.DEFAULT_ENCODING) as file:
            writer = csv.DictWriter(file,
                                    fieldnames=self.model.model_fields,
                                    dialect=constants.DEFAULT_DIALECT)
            writer.writerow(instance.model_dump())

        print(Fore.GREEN + constants.CONTACT_CREATED_MESSAGE)
        logging.info(f'{constants.CONTACT_CREATED_MESSAGE} - {instance}')

    def delete(self, row_id: int) -> None:
        """
        Удаляет объект из книги посредством перезаписывания всех контактов,
        кроме удаляемого во временный файл.
        Временный файл затем заменяет основной.

        Args:
            row_id (int): id контакта для удаления.
        """
        logging.info(f'Удаляю контакт с ID {row_id}')
        with open(self.phone_book,
                  mode='r',
                  encoding=constants.DEFAULT_ENCODING) as inp:
            reader = csv.reader(inp)
            try:
                file_row = next(islice(reader, row_id - 1, None))
            except StopIteration:
                print(Fore.RED + constants.CONTACT_NOT_FOUND_MESSAGE)
                logging.error(f'{constants.CONTACT_NOT_FOUND_MESSAGE}')
                exit(1)

            inp.seek(0)
            with open(constants.TEMP_FILE_NAME,
                      mode='w',
                      encoding=constants.DEFAULT_ENCODING) as out:
                writer = csv.writer(out, dialect=constants.DEFAULT_DIALECT)
                for row_id in reader:
                    if row_id != file_row:
                        writer.writerow(row_id)

        os.replace(constants.TEMP_FILE_NAME, self.phone_book)
        print(Fore.GREEN + constants.CONTACT_DELETED_MESSAGE)
        logging.info(constants.CONTACT_DELETED_MESSAGE)

    def update(self, row_id: int, instance: BaseModel) -> None:
        """
        Обновляет контакт посредством перезаписывания всех контактов
        во временный файл, а изменяемый - перезаписывается.
        Временный файл затем заменяет основной.

        Args:
            row_id (int): id контакта для обновления.
            instance (BaseModel): контакт, заменяющий старый.
        """
        with open(self.phone_book,
                  mode='r',
                  encoding=constants.DEFAULT_ENCODING) as inp:
            reader = csv.reader(inp)
            try:
                file_row = next(islice(reader, row_id - 1, None))
            except StopIteration:
                print(Fore.RED + constants.CONTACT_NOT_FOUND_MESSAGE)
                logging.error(f'{constants.CONTACT_NOT_FOUND_MESSAGE}')
                exit(1)

            inp.seek(0)
            with open(constants.TEMP_FILE_NAME,
                      mode='w',
                      encoding=constants.DEFAULT_ENCODING) as out:
                writer = csv.DictWriter(out,
                                        fieldnames=self.model.model_fields,
                                        dialect=constants.DEFAULT_DIALECT)
                for row_id in reader:
                    if row_id != file_row:
                        writer.writerow(row_id)
                    else:
                        writer.writerow(instance.model_dump())

        os.replace(constants.TEMP_FILE_NAME, self.phone_book)


book_crud = BookCrud(book_path=(constants.BASE_DIR /
                                constants.PHONE_BOOK_DIR_NAME /
                                constants.PHONE_BOOK_FILE_NAME),
                     model=Contact)
