import json
import logging
from argparse import Namespace
from copy import copy
from typing import KeysView

from prettytable import PrettyTable
from pydantic_extra_types.phone_numbers import PhoneNumber

from src import constants


class PhoneNumber(PhoneNumber):
    """
    Кастмный класс PhoneNumber для работы
    с Российскими номерами по умолчанию в Pydantic.
    """
    default_region_code = 'RU'
    phone_format = 'INTERNATIONAL'


def paginator(table: PrettyTable, page: int = 1) -> str:
    """
    Разделяет таблицу на страницы.
    Если такой страницы нет, возвращает сообщение.

    Args:
        table (PrettyTable): таблица с контактами.
        page (int, optional): желаемая страница. Defaults to 1.

    Returns:
        str: текст таблицы или сообщение об отсутствии такой страницы.
    """
    pages = table.paginate(page_length=constants.DEFAULT_PAGE_SIZE,
                           line_break='\0').split('\0')
    pages_length = len(pages)
    for num, pg in enumerate(pages):
        pages[num] = (
            constants.PAGINATOR_PAGE_MESSAGE.format(
                num=num + 1,
                pages_length=pages_length
            )
            + constants.PAGINATOR_PAGE_SELECT_HELP_MESSAGE
            + pg
        )

    return (pages[page - 1]
            if page <= (len(pages))
            else constants.PAGE_NOT_FOUND_MESSAGE)


def find_rows(book: PrettyTable,
              args: Namespace) -> tuple[list[list], KeysView]:
    """
    Находит в таблице записи с нужными данными.
    Переводит таблицу в JSON, из аргументов убираются пустые.
    Проверяет наличие полей в строках с данными из аргументов.

    Args:
        book (PrettyTable): таблица с контактами.
        args (Namespace): аргументы, полученные из парсера.

    Returns:
        tuple[list[dict], KeysView]: список со списками найденных контактов,
        а также название полей таблицы.
    """
    found = []
    args = vars(copy(args))
    args.pop('mode')
    args.pop('id')
    args.pop('page')
    field_names = book.field_names
    args = dict(zip(field_names[1:], args.values()))
    args = {k: v for k, v in args.items() if v is not None}
    logging.info(f'Начинаю поиск контактов с {args}')
    book.header = False
    book = book.get_formatted_string('json', ensure_ascii=False)
    book = json.loads(book)
    for row in book:
        if all(row.get(key).lower() == val.lower()
               for key, val in args.items()):
            found.append(list(row.values()))
    logging.info(f'Найдено следующее: {found}')

    return found, book[0].keys()
