from pydantic import BaseModel
from typing import Optional
from src.domain.enums.lesson.type import LessonType


class AdminLessonCreateDTO(BaseModel):
    module_id: str
    title: str
    type: LessonType = LessonType.TEXT
    content: Optional[str] = None
    video_url: Optional[str] = None
    duration: Optional[str] = None
    order_number: Optional[int] = None
    is_active: bool = True


class AdminLessonUpdateDTO(BaseModel):
    module_id: Optional[str] = None
    title: Optional[str] = None
    type: Optional[LessonType] = None
    content: Optional[str] = None
    video_url: Optional[str] = None
    duration: Optional[str] = None
    order_number: Optional[int] = None
    is_active: Optional[bool] = None
