from typing import Optional

from src.domain.enums.lesson import LessonType

from .base_entity import BaseEntity


class LessonEntity(BaseEntity):
    module_id: str
    title: str
    type: LessonType = LessonType.TEXT
    content: Optional[str] = None
    video_url: Optional[str] = None
    duration: Optional[str] = None
    order_number: Optional[int] = None
    is_active: bool = True

    class Settings:
        name = "lessons"
        indexes = [
            "module_id",
            [("module_id", 1), ("order_number", 1)]
        ]
