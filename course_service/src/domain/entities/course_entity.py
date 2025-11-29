from beanie import Document

from typing import Optional

from .base_entity import BaseEntity


class CourseEntity(BaseEntity):
    title: str
    description: Optional[str]
    preview_url: Optional[str] = None
    mentor_id: Optional[str] = None
    category_id: Optional[str] = None

    class Settings:
        name = "courses"
