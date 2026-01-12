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

    cover_image: Optional[str] = None
    author: Optional[dict] = None

    level: str
    duration_minutes: int = 0
    language: str
    requires_experience: bool = False

    price: CoursePriceSchema

    categories: list[dict] = []
    mentors: list[dict] = []

    rating: Optional[dict] = None
    lessons_count: int = 0

    sections: list[dict] = []


class CourseListItemSchema(BaseModel):
    id: str
    title: str
    description: Optional[str] = None

    cover_image: Optional[str] = None

    duration_minutes: int = 0
    language: str

    price: CoursePriceSchema

    category_ids: list[str] = []

    is_promoted: bool = False


class CourseListResponseSchema(BaseModel):
    items: list[CourseListItemSchema]
    total: int
