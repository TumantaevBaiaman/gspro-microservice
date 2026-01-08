from pydantic import BaseModel, EmailStr
from src.domain.enums.purchase_request import PurchaseTargetType


class CreatePurchaseRequestDTO(BaseModel):
    user_id: str | None = None
    email: EmailStr
    phone_number: str
    target_type: PurchaseTargetType
    target_id: str

