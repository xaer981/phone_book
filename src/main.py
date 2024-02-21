import logging
from argparse import Namespace

from prettytable import PrettyTable

from src import constants
from src.config import (configure_argument_parser, configure_logging,
                        configure_phone_book)
from src.conversation_handler import add_conversation
from src.crud import book_crud
from src.utils import find_rows, paginator
from src.validators import validate_page, validate_required_args


def get_all() -> PrettyTable:
    """
    Получает список контактов.

    Returns:
        PrettyTable: таблица с контактами.
    """

    return book_crud.get_all()


def add() -> None:
    """Добавляет контакт в таблицу."""
    contact = add_conversation()
    book_crud.add(contact)


def delete(row: int) -> None:
    """
    Удаляет контакт из таблицы.

    Args:
        row (int): id контакта для удаления.
    """
    book_crud.delete(row)


def update(row: int) -> None:
    """
    Обновляет контакт в таблице.
    Вызывает функцию запроса новых данных контакта и передаёт для обновления.

    Args:
        row (int): id контакта для обновления.
    """
    contact = add_conversation()
    book_crud.update(row_id=row, instance=contact)


def search(args: Namespace) -> PrettyTable:
    """
    Основная логика поиска.
    Получает всю таблицу контактов, находит подходящие.
    Затем формирует и выводит таблицу.

    Args:
        args (Namespace): аргументы для поиска.

    Returns:
        PrettyTable: таблица с найденными контактами.
    """
    book = get_all()
    found, field_names = find_rows(book, args)
    result = PrettyTable(field_names)
    result.add_rows(found)

    return result


MODE_TO_FUNCTION = {
    constants.GET_MODE_NAME: get_all,
    constants.ADD_MODE_NAME: add,
    constants.DELETE_MODE_NAME: delete,
    constants.UPDATE_MODE_NAME: update,
    constants.SEARCH_MODE_NAME: search,
}


def main() -> None:
    """
    Основная логика запуска приложения.
    Запускат конфигурацию логгера, телефонной книги и парсера.
    Если есть результаты работы - выводит их.
    """
    configure_logging()
    configure_phone_book()
    logging.info('Телефонная книга запущена!')

    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    validate_required_args(arg_parser, args)
    validate_page(arg_parser, args)
    logging.info(f'Аргументы: {args}')

    parser_mode = args.mode
    if parser_mode in constants.EDIT_METHODS:
        results = MODE_TO_FUNCTION[parser_mode](args.id)
    elif parser_mode == constants.GET_MODE_NAME:
        results = MODE_TO_FUNCTION[parser_mode]()
        results = paginator(results, args.page)
    elif parser_mode == 'search':
        results = MODE_TO_FUNCTION[parser_mode](args)
    else:
        results = MODE_TO_FUNCTION[parser_mode]()

    if results is not None:
        print(results)

    logging.info('Телефонная книга завершила работу.')


if __name__ == '__main__':
    main()
