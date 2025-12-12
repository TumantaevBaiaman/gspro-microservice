from pydantic import BaseModel
from typing import Optional
from src.domain.enums.city import City
from src.domain.enums.industry import Industry
from src.domain.enums.experience_level import ExperienceLevel


class UpdateProfileRequestDTO(BaseModel):
    full_name: Optional[str] = None
    bio: Optional[str] = None
    city: Optional[City] = None
    industry: Optional[Industry] = None
    experience_level: Optional[ExperienceLevel] = None


class GetProfileRequestDTO(BaseModel):
    user_id: str


class GetProfileResponseDTO(BaseModel):
    full_name: Optional[str] = None
    bio: Optional[str] = None
    city: Optional[City] = None
    industry: Optional[Industry] = None
    experience_level: Optional[ExperienceLevel] = None
