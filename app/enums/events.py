from enum import Enum, unique

@unique
class Event_type(str, Enum):
    PHYSICAL = "physical"
    VIRTUAL = "virtual"
@unique
class Event_categories(str, Enum):
    PRODUCT_LAUNCH = "product_launch"
    PRODUCT_REVIEW = "product_review"
@unique
class Event_frequency(str, Enum):
    SINGLE = "single"
    RECURRING = "recurring"
