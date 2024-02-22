from argparse import Namespace, ArgumentParser
from typing import Annotated

from pydantic import Field, TypeAdapter, ValidationError

from src import constants


def validate_required_args(arg_parser: ArgumentParser, parser_args: Namespace):
    """
    Проверяет передан ли необходимый аргумент для работы режимов изменения.

    Args:
        arg_parser (ArgumentParser): объект парсера.
        args (Namespace): переданные в парсер аргументы.
    """
    if parser_args.mode in constants.EDIT_METHODS and parser_args.id is None:
        arg_parser.error(constants.EDIT_METHODS_NO_REQUIRED_ARGS_MESSAGE)


def validate_page(arg_parser: ArgumentParser, parser_args: Namespace):
    """
    Проверяет, что страница больше нуля.

    Args:
        arg_parser (ArgumentParser): объект парсера.
        args (Namespace): переданные в парсер аргументы.
    """
    PositiveInt = Annotated[int, Field(gt=0)]
    ta = TypeAdapter(PositiveInt)
    if (parser_args.page is not None
            and parser_args.mode == constants.GET_MODE_NAME):
        try:
            ta.validate_python(parser_args.page)
        except ValidationError:
            arg_parser.error('Страница должна быть больше 0!')


def validate_at_least_one_search_param(arg_parser, parser_args):
    """
    Проверяет, что передан хотя бы один аргумент для поиска.

    Args:
        arg_parser (_type_): объект парсера.
        parser_args (_type_): переданные в парсер аргументы.
    """
    parser_args = vars(parser_args)
    if not any(parser_args.get(key) for key in constants.ADD_CONV_NAME_HELP):
        arg_parser.error(constants.SEARCH_NO_PARAMS_MESSAGE)
