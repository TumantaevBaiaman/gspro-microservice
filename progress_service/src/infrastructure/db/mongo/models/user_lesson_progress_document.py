from datetime import datetime
from typing import Optional

from .base import BaseDocument


class UserLessonProgressDocument(BaseDocument):
    user_id: str
    course_id: str
    module_id: str
    lesson_id: str

    watched_seconds: int = 0
    total_seconds: Optional[int] = None
    last_position_seconds: int = 0

    is_read: bool = False
    time_spent_seconds: int = 0
    scroll_percent: int = 0

    is_completed: bool = False
    completed_at: Optional[datetime] = None

    class Settings:
        name = "user_lesson_progress"
        indexes = [
            [("user_id", 1), ("lesson_id", 1)],
            [("user_id", 1), ("course_id", 1)],
            [("user_id", 1), ("module_id", 1)],
        ]
