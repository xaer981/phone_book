from argparse import Namespace, ArgumentParser

from src import constants


def validate_required_args(arg_parser: ArgumentParser, args: Namespace):
    if args.mode in constants.EDIT_METHODS and args.id is None:
        arg_parser.error('Необходимо передать номер записи '
                         'для редактирования (-i, --id)')
