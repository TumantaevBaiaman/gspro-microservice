from typing import Optional

from .base_entity import BaseEntity


class ModuleEntity(BaseEntity):
    course_id: str
    title: str
    description: Optional[str] = None
    order_number: Optional[int] = None
    duration_minutes: Optional[int] = None

    class Settings:
        name = "modules"
        indexes = [
            "course_id",
            [("course_id", 1), ("order_number", 1)]
        ]
