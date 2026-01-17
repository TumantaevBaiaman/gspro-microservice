from datetime import date
from .base import BaseDocument


class UserDailyLearningDocument(BaseDocument):
    user_id: str
    course_id: str

    learning_date: date

    class Settings:
        name = "user_daily_learning"
