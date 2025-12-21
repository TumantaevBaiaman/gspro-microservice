from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class SetUserImageRequestDTO(BaseModel):
    user_id: UUID
    original_url: str
    thumb_small_url: Optional[str]
    thumb_medium_url: Optional[str]


class SetUserImageResponseDTO(BaseModel):
    image_id: UUID

