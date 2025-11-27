from beanie import Document

from typing import Optional

from .base_entity import BaseEntity


class CourseEntity(BaseEntity):
    title: str
    description: Optional[str]
    preview_url: Optional[str]
    mentor_id: Optional[str]
    category_id: Optional[str]

    class Settings:
        name = "courses"
