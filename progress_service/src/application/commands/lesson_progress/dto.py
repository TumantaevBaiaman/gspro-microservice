from typing import Optional, Literal
from pydantic import BaseModel


class UpdateLessonProgressDTO(BaseModel):
    user_id: str

    course_id: str
    module_id: str
    lesson_id: str

    lesson_type: Literal["video", "text"]

    current_time: Optional[int] = None
    duration_seconds: Optional[int] = None

    last_scroll_percent: Optional[int] = None
