from pydantic import BaseModel, Field

from src.utils import PhoneNumber


class Contact(BaseModel):
    first_name: str = Field(title='Имя')
    last_name: str = Field(title='Фамилия', default='')
    father_name: str = Field(title='Отчество', default='')
    company: str = Field(title='Название организации', default='')
    number: PhoneNumber = Field(title='Номер телефона')
    work_number: PhoneNumber | str = Field(title='Рабочий номер телефона',
                                           default='')
