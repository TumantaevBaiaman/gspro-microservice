from pydantic import Field, EmailStr
from .base import BaseDocument
from src.domain.enums.purchase_request import (
    PurchaseTargetType,
    PurchaseRequestStatus,
)


class PurchaseRequestDocument(BaseDocument):
    user_id: str | None = None

    email: EmailStr
    phone_number: str
    telegram: str | None = None

    target_type: PurchaseTargetType
    target_id: str

    status: PurchaseRequestStatus = Field(
        default=PurchaseRequestStatus.PENDING
    )

    class Settings:
        name = "purchase_requests"
