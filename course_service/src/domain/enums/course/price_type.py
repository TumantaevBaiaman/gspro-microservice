from enum import Enum


class PriceType(str, Enum):
    FREE = "free"
    PAID = "paid"
    MIXED = "mixed"
