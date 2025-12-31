from typing import Optional, List
from pydantic import BaseModel, Field

from src.domain.enums.course.level import CourseLevel
from src.domain.enums.course.language import CourseLanguage
from src.domain.entities.course_entity import CoursePrice


class AdminCourseCreateDTO(BaseModel):
    title: str
    description: Optional[str] = None
    cover_image_id: Optional[str] = None

    author_id: Optional[str] = None

    level: CourseLevel
    duration_minutes: int = 0
    language: CourseLanguage = CourseLanguage.RU
    requires_experience: bool = False

    price: CoursePrice = Field(default_factory=CoursePrice)

    category_ids: List[str] = Field(default_factory=list)
    mentor_ids: List[str] = Field(default_factory=list)


class AdminCourseUpdateDTO(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

    level: Optional[CourseLevel] = None
    duration_minutes: Optional[int] = None
    language: Optional[CourseLanguage] = None
    requires_experience: Optional[bool] = None

    price: Optional[CoursePrice] = None

    category_ids: Optional[List[str]] = None
    mentor_ids: Optional[List[str]] = None
