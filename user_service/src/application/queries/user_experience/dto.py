from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime


class UserExperienceResponseDTO(BaseModel):
    id: UUID
    user_id: UUID

    company: str
    position: str

    start_date: date
    end_date: date | None
    description: str | None

    created_at: datetime

    class Config:
        from_attributes = True
