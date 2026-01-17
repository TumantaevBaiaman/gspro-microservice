from typing import Optional, Literal
from .base import BaseDocument


class UserLessonProgressDocument(BaseDocument):
    user_id: str

    course_id: str
    module_id: str
    lesson_id: str

    lesson_type: str

    watched_seconds: int | None = None
    duration_seconds: Optional[int] = None
    last_position_seconds: int = 0

    last_scroll_percent: Optional[int] = None

    is_completed: bool = False

    class Settings:
        name = "user_lesson_progress"
