from pydantic import BaseModel
from typing import Optional


class CoursePriceDTO(BaseModel):
    type: str
    amount: Optional[int] = 0


class GetCourseRequestDTO(BaseModel):
    id: str


class GetCourseResponseDTO(BaseModel):
    id: str
    title: str
    description: Optional[str] = None

    level: str
    duration_minutes: int = 0
    language: str
    requires_experience: bool = False

    price: CoursePriceDTO

    category_ids: list[str] = []
    mentor_ids: list[str] = []


class ListCoursesRequestDTO(BaseModel):
    limit: int = 10
    offset: int = 0


class CourseListItemDTO(BaseModel):
    id: str
    title: str
    description: Optional[str] = None

    level: str
    duration_minutes: int = 0
    language: str
    requires_experience: bool = False

    price: CoursePriceDTO

    category_ids: list[str] = []
    mentor_ids: list[str] = []


class ListCoursesResponseDTO(BaseModel):
    items: list[CourseListItemDTO]
    total: int
