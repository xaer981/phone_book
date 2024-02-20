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
        pages[num] = f'\nСтраница {num + 1} из {pages_length}\n' + pg

    return (pages[page - 1]
            if page <= (len(pages))
            else constants.PAGE_NOT_FOUND_MESSAGE)
