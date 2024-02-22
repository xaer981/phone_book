from pathlib import Path

# Path
BASE_DIR = Path(__file__).parent
LOG_DIR_NAME = 'logs'
LOG_FILE_NAME = 'phone_book.log'
PHONE_BOOK_DIR_NAME = 'book'
PHONE_BOOK_FILE_NAME = 'phone_book'
TEMP_FILE_NAME = 'temp.csv'

# App
ADD_MODE_NAME = 'add'
APP_DESCRIPTION = 'Телефонная книга для консоли'
COMPANY_ARG_SHORT_NAME = '-c'
COMPANY_ARG_FULL_NAME = '--company'
COMPANY_ARG_METAVAR = 'Effective Mobile'
COMPANY_HELP_MESSAGE = 'Компания контакта'
CONTACT_CREATED_MESSAGE = 'Контакт создан!'
CONTACT_DELETED_MESSAGE = 'Запись удалена!'
CONTACT_NOT_FOUND_MESSAGE = 'Контакта с таким номером не нашлось'
CONTACT_UPDATED_MESSAGE = 'Контакт обновлен!'
DELETE_MODE_NAME = 'delete'
FATHER_NAME_ARG_SHORT_NAME = '-fr'
FATHER_NAME_ARG_FULL_NAME = '--father_name'
FATHER_NAME_ARG_METAVAR = 'Игоревич'
FATHER_NAME_HELP_MESSAGE = 'Отчество контакта'
FIRST_NAME_ARG_SHORT_NAME = '-f'
FIRST_NAME_ARG_FULL_NAME = '--first_name'
FIRST_NAME_ARG_METAVAR = 'Андрей'
FIRST_NAME_HELP_MESSAGE = 'Имя контакта'
GET_MODE_NAME = 'get-all'
LAST_NAME_ARG_SHORT_NAME = '-l'
LAST_NAME_ARG_FULL_NAME = '--last_name'
LAST_NAME_ARG_METAVAR = 'Петров'
LAST_NAME_HELP_MESSAGE = 'Фамилия контакта'
MODE_ARG_NAME = 'mode'
MODES_HELP_MESSAGE = 'Режим работы телефонной книги'
NUMBER_ARG_SHORT_NAME = '-n'
NUMBER_ARG_FULL_NAME = '--number'
NUMBER_ARG_METAVAR = '+7 999 123 45 67'
NUMBER_HELP_MESSAGE = 'Номер контакта'
PAGE_ARG_SHORT_NAME = '-p'
PAGE_ARG_FULL_NAME = '--page'
PAGE_HELP_MESSAGE = 'Параметр для выбора страницы при просмотре книги'
PAGINATOR_PAGE_SELECT_HELP_MESSAGE = (f'Для выбора страницы используйте '
                                      f'{PAGE_ARG_SHORT_NAME} '
                                      f'({PAGE_ARG_FULL_NAME})\n')
PAGINATOR_PAGE_MESSAGE = '\nСтраница {num} из {pages_length}. '
PHONE_BOOK_EMPTY_MESSAGE = 'Телефонная книга пуста'
ROW_HELP_MESSAGE = 'Параметр для выбора записи при удалении/редактировании'
ROW_ARG_SHORT_NAME = '-i'
ROW_ARG_FULL_NAME = '--id'
ROW_ARG_MAX_USES = 1
EDIT_METHODS_NO_REQUIRED_ARGS_MESSAGE = (f'Необходимо передать '
                                         f'номер записи для редактирования '
                                         f'({ROW_ARG_SHORT_NAME}, '
                                         f'{ROW_ARG_FULL_NAME})')
SEARCH_MODE_NAME = 'search'
SEARCH_MODE_HELP_MESSAGE = ('Параметры для поиска контакта. '
                            'Можно указать любое количество '
                            'критериев для поиска.')
SEARCH_NO_PARAMS_MESSAGE = ('Необходимо передать хотя бы '
                            'один параметр для поиска!')
UPDATE_MODE_NAME = 'update'
WORK_NUMBER_ARG_SHORT_NAME = '-wn'
WORK_NUMBER_ARG_FULL_NAME = '--work_number'
WORK_NUMBER_ARG_METAVAR = '+7 999 765 43 21'
WORK_NUMBER_HELP_MESSAGE = 'Рабочий номер контакта'
EDIT_METHODS = (UPDATE_MODE_NAME, DELETE_MODE_NAME)

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

# Utils
DEFAULT_ENCODING = 'utf-8'
DEFAULT_DIALECT = 'unix'
DEFAULT_PAGE_SIZE = 5
PAGE_NOT_FOUND_MESSAGE = 'Страницы с таким номером нет.'

# Logs
LOG_DT_FORMAT = '%d.%m.%Y %H:%M:%S'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
