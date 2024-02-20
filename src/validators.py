from argparse import Namespace, ArgumentParser
from typing import Annotated

from pydantic import Field, TypeAdapter, ValidationError

from src import constants


def validate_required_args(arg_parser: ArgumentParser, args: Namespace):
    """
    Проверяет передан ли необходимый аргумент для работы режимой изменения.

    Args:
        arg_parser (ArgumentParser): объект парсера.
        args (Namespace): переданные в парсер аргументы.
    """
    if args.mode in constants.EDIT_METHODS and args.id is None:
        arg_parser.error('Необходимо передать номер записи '
                         'для редактирования (-i, --id)')


def validate_page(arg_parser: ArgumentParser, args: Namespace):
    """
    Проверяет, что страница больше нуля.

    Args:
        arg_parser (ArgumentParser): объект парсера.
        args (Namespace): переданные в парсер аргументы.
    """
    PositiveInt = Annotated[int, Field(gt=0)]
    ta = TypeAdapter(PositiveInt)
    if args.page is not None and args.mode == constants.GET_MODE_NAME:
        try:
            ta.validate_python(args.page)
        except ValidationError:
            arg_parser.error('Страница должна быть больше 0!')
