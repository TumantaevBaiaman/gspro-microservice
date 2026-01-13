from typing import Optional, Literal
from .base import BaseDocument


class UserLessonProgressDocument(BaseDocument):
    user_id: str

    course_id: str
    module_id: str
    lesson_id: str

    lesson_type: str

    watched_seconds: int = 0
    duration_seconds: Optional[int] = None
    last_position_seconds: int = 0

    last_scroll_percent: Optional[int] = None

    is_completed: bool = False

    class Settings:
        name = "user_lesson_progress"
        indexes = [
            {"keys": [("user_id", 1), ("lesson_id", 1)], "unique": True},

            [("user_id", 1), ("course_id", 1)],
            [("user_id", 1), ("module_id", 1)],
        ]
