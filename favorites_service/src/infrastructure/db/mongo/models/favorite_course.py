from .base import BaseDocument


class FavoriteCourseDocument(BaseDocument):
    user_id: str
    course_id: str

    class Settings:
        name = "favorite_courses"
