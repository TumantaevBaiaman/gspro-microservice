from .base import BaseDocument


class CourseAccessDocument(BaseDocument):
    user_id: str
    course_id: str

    class Settings:
        name = "course_accesses"
        indexes = [
            [("user_id", 1), ("course_id", 1)],
        ]
