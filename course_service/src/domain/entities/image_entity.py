from typing import Optional

from .base_entity import BaseEntity
from src.domain.enums.image_type import ImageType


class ImageEntity(BaseEntity):
    type: ImageType

    original_url: str
    thumb_small_url: Optional[str] = None
    thumb_medium_url: Optional[str] = None

    class Settings:
        name = "images"
