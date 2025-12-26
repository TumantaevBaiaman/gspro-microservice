from pydantic import BaseModel, Field
from datetime import datetime


class CreateUserCertificateDTO(BaseModel):
    title: str = Field(..., max_length=255)
    issuer: str | None = Field(default=None, max_length=255)
    issued_at: datetime | None = None
    link: str | None = None
