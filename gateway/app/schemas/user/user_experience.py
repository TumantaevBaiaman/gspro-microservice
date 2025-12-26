from pydantic import BaseModel, Field
from uuid import UUID
from datetime import date, datetime


class CreateUserExperienceSchema(BaseModel):
    company: str
    position: str
    start_date: date
    end_date: date | None = None
    description: str | None = None


class UserExperienceItemSchema(BaseModel):
    id: UUID
    user_id: UUID

    company: str
    position: str

    start_date: date
    end_date: date | None
    description: str | None

    created_at: datetime


class ListUserExperiencesResponseSchema(BaseModel):
    items: list[UserExperienceItemSchema] = Field(default_factory=list)
    total: int = 0
