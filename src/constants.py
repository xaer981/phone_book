from pathlib import Path

# Path
BASE_DIR = Path(__file__).parent
LOG_DIR_NAME = 'logs'
LOG_FILE_NAME = 'phone_book.log'
PHONE_BOOK_DIR_NAME = 'book'
PHONE_BOOK_FILE_NAME = 'phone_book'

# Parser
APP_DESCRIPTION = 'Телефонная книга для консоли'
MODE_ARG_NAME = 'mode'
MODES_HELP_MESSAGE = 'Режим работы телефонной книги'
ROW_HELP_MESSAGE = 'Параметр для выбора записи при удалении/редактировании'
ROW_ARG_SHORT_NAME = '-i'
ROW_ARG_FULL_NAME = '--id'
ROW_ARG_MAX_USES = 1
EDIT_METHODS = ('update', 'delete')

# Conversation
ADD_CONV_NAME_HELP = {
    'first_name': ('Введите имя контакта',
                   True),
    'last_name': ('Введите фамилию контакта или оставьте поле пустым',
                  False),
    'father_name': ('Введите отчество контакта или оставьте поле пустым',
                    False),
    'company': ('Введите название организации контакта '
                'или оставьте поле пустым',
                False),
    'number': ('Введите номер телефона контакта',
               True),
    'work_number': ('Введите рабочий номер телефона контакта '
                    'или оставьте поле пустым',
                    False),
}
ABORT_EXIT_MESSAGE = '\nПроцесс создания контакта остановлен'

# Logs
LOG_DT_FORMAT = '%d.%m.%Y %H:%M:%S'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
