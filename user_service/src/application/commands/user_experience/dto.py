from pydantic import BaseModel, Field
from datetime import date


class CreateUserExperienceDTO(BaseModel):
    company: str = Field(..., max_length=255)
    position: str = Field(..., max_length=255)

    start_date: date
    end_date: date | None = None

    description: str | None = None
