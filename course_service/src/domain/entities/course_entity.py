from typing import Optional, List
from pydantic import BaseModel, Field, model_validator

from .base_entity import BaseEntity
from src.domain.enums.course.language import CourseLanguage
from src.domain.enums.course.level import CourseLevel
from src.domain.enums.course.price_type import PriceType


class CoursePrice(BaseModel):
    type: PriceType
    amount: Optional[int] = None


class CourseEntity(BaseEntity):
    title: str
    description: Optional[str] = None

    level: CourseLevel = CourseLevel.BEGINNER
    duration_minutes: int = 0
    language: CourseLanguage = CourseLanguage.RU
    requires_experience: bool = False

    price: CoursePrice = Field(default_factory=CoursePrice)

    category_ids: Optional[List[str]] = Field(default_factory=list)
    mentor_ids: Optional[List[str]] = Field(default_factory=list)

    class Settings:
        name = "courses"
