import csv
import os
from itertools import islice
from operator import attrgetter
from pathlib import Path

from prettytable import PrettyTable, from_csv

from src import constants
from src.schemas import Contact


class BookCrud:
    def __init__(self, book_path: Path) -> None:
        self.phone_book = book_path.with_suffix('.csv')

    def get_all(self) -> PrettyTable:
        contact_titles = map(attrgetter('title'),
                             Contact.model_fields.values())
        try:
            with open(self.phone_book, mode='r', encoding='utf-8') as file:
                table = from_csv(file, field_names=contact_titles)
                table.add_autoindex('ID')

        except csv.Error:
            print('Телефонная книга пуста')
            exit(1)

        return table

    def add(self, instance: Contact) -> None:
        with open(self.phone_book, mode='a', encoding='utf-8') as file:
            writer = csv.DictWriter(file,
                                    fieldnames=Contact.model_fields,
                                    dialect='unix')
            writer.writerow(instance.model_dump())

    def delete(self, row: int) -> None:
        with open(self.phone_book, mode='r', encoding='utf-8') as inp:
            reader = csv.reader(inp)
            try:
                file_row = next(islice(reader, row - 1, None))
            except StopIteration:
                print('Контакта с таким номером не нашлось')
                exit(1)

            inp.seek(0)
            with open('edit.csv', 'w', encoding='utf-8') as out:
                writer = csv.writer(out, dialect='unix')
                for row in reader:
                    if row != file_row:
                        writer.writerow(row)

        os.replace('edit.csv', self.phone_book)
        print('Запись удалена')


book_crud = BookCrud(book_path=(constants.BASE_DIR /
                                constants.PHONE_BOOK_DIR_NAME /
                                constants.PHONE_BOOK_FILE_NAME))
