from .base import BaseDocument


class UserModuleProgressDocument(BaseDocument):
    user_id: str
    course_id: str
    module_id: str

    completed_lessons: int = 0
    total_lessons: int = 0

    progress_percent: float = 0.0
    is_completed: bool = False

    class Settings:
        name = "user_module_progress"
        indexes = [
            [("user_id", 1), ("module_id", 1)],
            [("user_id", 1), ("course_id", 1)],
        ]
