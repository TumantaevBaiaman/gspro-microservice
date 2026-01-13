from datetime import date
from .base import BaseDocument


class UserDailyLearningDocument(BaseDocument):
    user_id: str
    course_id: str

    learning_date: date

    class Settings:
        name = "user_daily_learning"
        indexes = [
            {
                "keys": [("user_id", 1), ("course_id", 1), ("learning_date", 1)],
                "unique": True
            },

            [("user_id", 1), ("learning_date", 1)],
        ]
