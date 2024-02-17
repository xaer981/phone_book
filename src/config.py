import argparse
import logging
from logging.handlers import RotatingFileHandler

from src import constants


def configure_argument_parser(available_modes) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=constants.APP_DESCRIPTION)
    parser.add_argument(constants.MODE_ARG_NAME,
                        choices=available_modes,
                        help=constants.MODES_HELP_MESSAGE)
    parser.add_argument(constants.ROW_ARG_SHORT_NAME,
                        constants.ROW_ARG_FULL_NAME,
                        type=int,
                        nargs=constants.ROW_ARG_MAX_USES)

    return parser


def configure_logging() -> None:
    log_dir = (constants.BASE_DIR / constants.LOG_DIR_NAME)
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
