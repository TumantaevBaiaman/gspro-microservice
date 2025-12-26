from datetime import date
from typing import Optional

from pydantic import BaseModel


class AvatarSchema(BaseModel):
    original_url: str
    thumb_small_url: str | None = None
    thumb_medium_url: str | None = None


class GetUserProfileResponseSchema(BaseModel):
    email: str
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    bio: Optional[str] = None
    date_of_birth: Optional[str] = None
    avatar: AvatarSchema | None = None
    city: Optional[str] = None
    industry: Optional[str] = None
    experience_level: Optional[str] = None


class UpdateUserProfileRequestSchema(BaseModel):
    full_name: Optional[str] = None
    bio: Optional[str] = None
    date_of_birth: Optional[date] = None
    city: Optional[str] = None
    industry: Optional[str] = None
    experience_level: Optional[str] = None


class UpdateUserProfileResponseSchema(BaseModel):
    success: bool


class UserProfileListItemSchema(BaseModel):
    user_id: str
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    city: Optional[str] = None
    industry: Optional[str] = None
    experience_level: Optional[str] = None


class ListUserProfilesResponseSchema(BaseModel):
    items: list[UserProfileListItemSchema]
    total: int


class SetAvatarResponseSchema(BaseModel):
    image_id: str