from pydantic_extra_types.phone_numbers import PhoneNumber


class PhoneNumber(PhoneNumber):
    default_region_code = 'RU'
    phone_format = 'INTERNATIONAL'
