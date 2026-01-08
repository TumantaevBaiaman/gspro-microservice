from enum import Enum


class PurchaseTargetType(str, Enum):
    COURSE = "course"


class PurchaseRequestStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    REJECTED = "rejected"
    CANCELED = "canceled"
