from typing import Optional
from pydantic import BaseModel


class CourseGetRequestSchema(BaseModel):
    id: str


class CoursePriceSchema(BaseModel):
    type: str
    amount: int = 0


class CourseGetResponseSchema(BaseModel):
    id: str
    title: str
    description: Optional[str] = None

    level: str
    duration_minutes: int = 0
    language: str
    requires_experience: bool = False

    price: CoursePriceSchema

    category_ids: list[str] = []
    mentor_ids: list[str] = []


class CourseListItemSchema(BaseModel):
    id: str
    title: str
    description: Optional[str] = None

    level: str
    duration_minutes: int = 0
    language: str
    requires_experience: bool = False

    price: CoursePriceSchema

    category_ids: list[str] = []
    mentor_ids: list[str] = []


class CourseListResponseSchema(BaseModel):
    items: list[CourseListItemSchema]
    total: int
