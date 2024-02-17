from pathlib import Path

# Path
BASE_DIR = Path(__file__).parent
LOG_DIR_NAME = 'logs'
LOG_FILE_NAME = 'phone_book.log'
PHONE_BOOK_DIR_NAME = 'book'

# Parser
APP_DESCRIPTION = 'Телефонная книга для консоли'
MODE_ARG_NAME = 'mode'
MODES_HELP_MESSAGE = 'Режим работы телефонной книги'
ROW_ARG_SHORT_NAME = '-r'
ROW_ARG_FULL_NAME = '--row'
ROW_ARG_MAX_USES = 1

# Logs
LOG_DT_FORMAT = '%d.%m.%Y %H:%M:%S'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
