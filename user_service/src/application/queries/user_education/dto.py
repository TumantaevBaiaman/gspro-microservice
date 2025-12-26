from pydantic import BaseModel
from uuid import UUID


class UserEducationResponseDTO(BaseModel):
    id: UUID
    user_id: UUID
    institution: str
    degree: str | None
    start_year: int | None
    end_year: int | None

    class Config:
        from_attributes = True
        