from pydantic import BaseModel, Field
from typing import Literal


class CreateAppFeedbackSchema(BaseModel):
    message: str = Field(..., max_length=300)
    type: Literal["feedback"] = "feedback"
    is_public: bool | None = False


class AppFeedbackSchema(BaseModel):
    id: str
    user_id: str
    message: str
    type: str
    is_public: bool = False


class AppFeedbackListSchema(BaseModel):
    items: list[AppFeedbackSchema]
    total: int

