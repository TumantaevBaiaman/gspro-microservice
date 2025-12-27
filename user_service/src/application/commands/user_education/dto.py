from pydantic import BaseModel, Field


class CreateUserEducationDTO(BaseModel):
    institution: str = Field(..., max_length=255)
    degree: str | None = Field(default=None, max_length=255)
    start_year: int | None = None
    end_year: int | None = None
