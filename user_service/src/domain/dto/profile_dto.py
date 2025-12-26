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


class AvatarDTO(BaseModel):
    original_url: str
    thumb_small_url: Optional[str]
    thumb_medium_url: Optional[str]

    model_config = {
        "arbitrary_types_allowed": True
    }


class GetProfileRequestDTO(BaseModel):
    user_id: str


class GetProfileResponseDTO(BaseModel):
    email: str
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    bio: Optional[str] = None
    date_of_birth: Optional[str] = None
    city: Optional[City] = None
    industry: Optional[Industry] = None
    experience_level: Optional[ExperienceLevel] = None
    avatar: Optional[AvatarDTO] = None


class ListProfilesRequestDTO(BaseModel):
    limit: int = 10
    offset: int = 0


class ListProfilesItemDTO(BaseModel):
    user_id: str
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    city: Optional[City] = None
    industry: Optional[Industry] = None
    experience_level: Optional[ExperienceLevel] = None


class ListProfilesResponseDTO(BaseModel):
    items: list[ListProfilesItemDTO]
    total: int


class ListProfilesByIdsRequestDTO(BaseModel):
    user_ids: list[str] = []


class ListProfilesByIdsItemDTO(BaseModel):
    user_id: str
    full_name: Optional[str] = None
    bio: Optional[str] = None
    industry: Optional[Industry] = None
    experience_level: Optional[ExperienceLevel] = None
    avatar: Optional[AvatarDTO] = None


class ListProfilesByIdsResponseDTO(BaseModel):
    items: list[ListProfilesByIdsItemDTO]

