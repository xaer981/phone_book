import logging

from src import constants
from src.config import (configure_argument_parser, configure_logging,
                        configure_phone_book)
from src.conversation_handler import add_conversation
from src.crud import book_crud
from src.validators import validate_required_args


def get_all():

    return book_crud.get_all()


def add():
    contact = add_conversation()
    book_crud.add(contact)
    print('Контакт создан!')


def delete(row: int):
    book_crud.delete(row)


MODE_TO_FUNCTION = {
    'get-all': get_all,
    'add': add,
    'delete': delete,
}


def main() -> None:
    configure_logging()
    configure_phone_book()
    logging.info('Телефонная книга запущена!')

    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    validate_required_args(arg_parser, args)
    logging.info(f'Аргументы: {args}')

    parser_mode = args.mode
    if parser_mode in constants.EDIT_METHODS:
        results = MODE_TO_FUNCTION[parser_mode](args.id)
    else:
        results = MODE_TO_FUNCTION[parser_mode]()

    if results is not None:
        print(results)

    logging.info('Телефонная книга завершила работу.')


if __name__ == '__main__':
    main()
