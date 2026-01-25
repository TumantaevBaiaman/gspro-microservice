from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class CreateUserCertificateSchema(BaseModel):
    title: str
    issuer: str | None = None
    issued_at: datetime | None = None
    link: str | None = None


class UserCertificateItemSchema(BaseModel):
    id: UUID
    user_id: UUID

    title: str
    issuer: str | None = None
    issued_at: datetime | None = None
    link: str | None = None
    created_at: datetime


class ListUserCertificatesResponseSchema(BaseModel):
    items: list[UserCertificateItemSchema] = Field(default_factory=list)
    total: int = 0
