import click
from colorama import Fore, init

from src import constants
from src.schemas import Contact


def add_conversation() -> Contact:
    raw_contact = dict()
    try:
        for name, data in constants.ADD_CONV_NAME_HELP.items():
            help_msg, required = data
            raw_contact[name] = click.prompt((Fore.GREEN + help_msg),
                                             type=click.STRING,
                                             default=None if required else '')
    except click.exceptions.Abort:
        init(autoreset=True)
        print(Fore.RED + constants.ABORT_EXIT_MESSAGE)
        exit(130)

    return Contact.model_validate(raw_contact)
