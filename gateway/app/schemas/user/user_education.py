from pydantic import BaseModel, Field
from uuid import UUID


class CreateUserEducationSchema(BaseModel):
    institution: str
    degree: str | None = None
    start_year: int | None = None
    end_year: int | None = None


class UserEducationItemSchema(BaseModel):
    id: UUID
    user_id: UUID
    institution: str
    degree: str | None
    start_year: int | None = None
    end_year: int | None = None


class ListUserEducationsResponseSchema(BaseModel):
    items: list[UserEducationItemSchema] = Field(default_factory=list)
    total: int = 0
