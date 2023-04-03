from enum import Enum, unique


@unique
class Transaction_status(str, Enum):
    SUCCESSFUL = 'Successful'
    PENDING = 'Pending'
    FAILED = 'Failed'
