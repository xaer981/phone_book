import argparse
import logging
from logging.handlers import RotatingFileHandler
from typing import KeysView

from src import constants


def configure_argument_parser(
    available_modes: KeysView
) -> argparse.ArgumentParser:
    """
    Запускает конфигурацию парсера.
    Добавляет три аргумента: доступные режимы,
    номер записи для удаления/изменения,
    номер страницы для просмотра.

    Args:
        available_modes (KeysView): доступные режимы работы.

    Returns:
        argparse.ArgumentParser: парсер аргументов.
    """
    parser = argparse.ArgumentParser(description=constants.APP_DESCRIPTION)
    parser.add_argument(constants.MODE_ARG_NAME,
                        choices=available_modes,
                        help=constants.MODES_HELP_MESSAGE)
    parser.add_argument(constants.ROW_ARG_SHORT_NAME,
                        constants.ROW_ARG_FULL_NAME,
                        type=int,
                        help=constants.ROW_HELP_MESSAGE)
    parser.add_argument(constants.PAGE_ARG_SHORT_NAME,
                        constants.PAGE_ARG_FULL_NAME,
                        type=int,
                        default=1,
                        help=constants.PAGE_HELP_MESSAGE)
    subparser = parser.add_argument_group('search',
                                          ('Параметры для поиска контакта. '
                                           'Можно указать любое количество '
                                           'критериев для поиска.'))
    subparser.add_argument('-f',
                           '--first_name',
                           metavar='Андрей',
                           default='',
                           help='Имя контакта')
    subparser.add_argument('-l',
                           '--last_name',
                           metavar='Петров',
                           default='',
                           help='Фамилия контакта')
    subparser.add_argument('-fr',
                           '--father_name',
                           metavar='Игоревич',
                           default='',
                           help='Отчество контакта')
    subparser.add_argument('-c',
                           '--company',
                           metavar='Effective Mobile',
                           default='',
                           help='Компания контакта')
    subparser.add_argument('-n',
                           '--number',
                           metavar='+7 999 123 45 67',
                           default='',
                           help='Номер контакта')
    subparser.add_argument('-wn',
                           '--work_number',
                           metavar='+7 999 765 43 21',
                           default='',
                           help='Рабочий номер контакта')

    return parser


def configure_phone_book() -> None:
    """Создаёт необходимые папки и файл телефонной книги."""
    phone_book_dir = constants.BASE_DIR / constants.PHONE_BOOK_DIR_NAME
    phone_book_dir.mkdir(parents=True, exist_ok=True)
    phone_book_file = ((phone_book_dir / constants.PHONE_BOOK_FILE_NAME)
                       .with_suffix('.csv'))
    phone_book_file.touch(exist_ok=True)


def configure_logging() -> None:
    """Запускает конфигурацию логгера, создаёт папки для логов."""
    log_dir = constants.BASE_DIR / constants.LOG_DIR_NAME
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / constants.LOG_FILE_NAME

    rotating_handler = RotatingFileHandler(log_file,
                                           maxBytes=10 ** 6,
                                           backupCount=5,
                                           encoding='utf-8')

    logging.basicConfig(datefmt=constants.LOG_DT_FORMAT,
                        format=constants.LOG_FORMAT,
                        level=logging.INFO,
                        handlers=(rotating_handler,))
