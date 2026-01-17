from pydantic import BaseModel
from typing import Optional, List


class UpdateLessonProgressRequestSchema(BaseModel):
    course_id: str
    module_id: str
    lesson_id: str
    lesson_type: str  # video | text
    current_time: Optional[int] = None
    duration_seconds: Optional[int] = None
    last_scroll_percent: Optional[int] = None


class LessonProgressResponseSchema(BaseModel):
    user_id: str
    course_id: str
    module_id: str
    lesson_id: str
    lesson_type: str
    watched_seconds: int
    duration_seconds: Optional[int] = None
    last_position_seconds: Optional[int] = None
    last_scroll_percent: Optional[int] = None
    is_completed: bool = False



class GetLessonProgressResponseSchema(BaseModel):
    lesson_id: str
    last_position_seconds: Optional[int] = None
    last_scroll_percent: Optional[int] = None
    is_completed: Optional[bool] = False


class CompletedLessonsCountResponseSchema(BaseModel):
    completed_lessons: int


class LearningDaysResponseSchema(BaseModel):
    days: List[str]
    from_date: str
    to_date: str
    count: int
