from pydantic import BaseModel, EmailStr


class CreatePurchaseRequestSchema(BaseModel):
    email: EmailStr
    phone_number: str
    target_type: str
    target_id: str


class UpdatePurchaseRequestStatusSchema(BaseModel):
    status: str


class PurchaseRequestResponseSchema(BaseModel):
    id: str
    user_id: str | None
    email: str
    phone_number: str
    target_type: str
    target_id: str
    status: str


class PurchaseRequestListResponseSchema(BaseModel):
    items: list[PurchaseRequestResponseSchema]
    total: int
