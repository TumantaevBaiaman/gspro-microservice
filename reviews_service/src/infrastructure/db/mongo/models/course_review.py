from .base import BaseDocument


class CourseReviewDocument(BaseDocument):
    course_id: str
    user_id: str

    rating: int
    comment: str
    tags: list[str]

    class Settings:
        name = "course_reviews"
