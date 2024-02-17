from pydantic import BaseModel

from utils import PhoneNumber


class Contact(BaseModel):
    first_name: str
    last_name: str = None
    father_name: str = None
    company: str = None
    number: PhoneNumber
    work_number: PhoneNumber = None
