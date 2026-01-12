from datetime import datetime
from typing import Optional

from src.infrastructure.db.mongo.models.base import BaseDocument


class UserCourseProgressDocument(BaseDocument):
    user_id: str
    course_id: str

    completed_modules: int = 0
    total_modules: int = 0

    progress_percent: float = 0.0

    is_completed: bool = False
    completed_at: Optional[datetime] = None

    last_lesson_id: Optional[str] = None

    class Settings:
        name = "user_course_progress"
        indexes = [
            [("user_id", 1), ("course_id", 1)],
        ]
