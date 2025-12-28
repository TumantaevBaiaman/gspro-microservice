from pydantic import BaseModel
from typing import Literal


class CreateAppFeedbackDTO(BaseModel):
    user_id: str
    message: str
    type: Literal["feedback", "bug", "suggestion"] = "feedback"
    is_public: bool = False
