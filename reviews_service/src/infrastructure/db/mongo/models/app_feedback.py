from .base import BaseDocument


class AppFeedbackDocument(BaseDocument):
    user_id: str

    message: str
    type: str = "feedback"
    is_public: bool = False

    class Settings:
        name = "app_feedbacks"