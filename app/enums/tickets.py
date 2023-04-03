from enum import Enum, unique

@unique
class Ticket_type(str, Enum):
    FREE = 'Free'
    PAID = 'Paid'
    INVITE_ONLY = 'Invite_only'

@unique
class Ticket_stock(str, Enum):
    UNLIMITED = 'Unlimited'
    LIMITED = 'Limited'