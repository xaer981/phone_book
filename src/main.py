import logging

from src.config import configure_logging, configure_argument_parser


def get_all():
    print('Контакты...')


MODE_TO_FUNCTION = {
    'get-all': get_all,
}


def main() -> None:
    configure_logging()
    logging.info('Телефонная книга запущена!')

    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    logging.info(f'Аргументы: {args}')

    parser_mode = args.mode
    results = MODE_TO_FUNCTION[parser_mode]()

    if results is not None:
        pass

    logging.info('Телефонная книга завершила работу.')


if __name__ == '__main__':
    main()
