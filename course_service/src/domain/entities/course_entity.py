from typing import Optional, List
from pydantic import BaseModel, Field, model_validator

from .base_entity import BaseEntity
from src.domain.enums.course.language import CourseLanguage
from src.domain.enums.course.level import CourseLevel
from src.domain.enums.course.price_type import PriceType


class CoursePrice(BaseModel):
    type: PriceType
    amount: Optional[int] = None


class CourseSection(BaseModel):
    title: str
    items: List[str]


class CourseEntity(BaseEntity):
    title: str
    description: Optional[str] = None

    sections: List[CourseSection] = Field(default_factory=list)

    cover_image_id: Optional[str] = None

    author_id: Optional[str] = None

    level: CourseLevel = CourseLevel.BEGINNER
    duration_minutes: int = 0
    language: CourseLanguage = CourseLanguage.RU
    requires_experience: bool = False

    price: CoursePrice = Field(
        default_factory=lambda: CoursePrice(
            type=PriceType.FREE,
            amount=0
        )
    )

    category_ids: Optional[List[str]] = Field(default_factory=list)
    mentor_ids: Optional[List[str]] = Field(default_factory=list)

    class Settings:
        name = "courses"
