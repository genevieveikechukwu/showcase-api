from enum import Enum, unique

@unique
class Country(str, Enum):
    NIGERIA = 'Nigeria'
    GHANA= 'Ghana'

@unique
class Acct_type(str, Enum):
    INDIVIDUAL = 'Individual'
    ORGANIZATION= 'Organization'