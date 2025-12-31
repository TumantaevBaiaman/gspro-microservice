from typing import Optional, List

from pydantic import BaseModel


class CoursePriceSchema(BaseModel):
    type: str
    amount: int = 0


class AdminCourseCreateRequestSchema(BaseModel):
    title: str
    description: Optional[str] = None
    cover_image_id: Optional[str] = None

    level: str = "beginner"
    duration_minutes: Optional[int] = 0
    language: str = "ru"
    requires_experience: Optional[bool] = False

    price: CoursePriceSchema

    category_ids: List[str] = []
    mentor_ids: List[str] = []


class AdminCourseCreateResponseSchema(BaseModel):
    id: str


class AdminCourseUpdateRequestSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

    level: Optional[str] = None
    duration_minutes: Optional[int] = None
    language: Optional[str] = None
    requires_experience: Optional[bool] = None

    price: Optional[CoursePriceSchema] = None

    category_ids: Optional[List[str]] = None
    mentor_ids: Optional[List[str]] = None


class AdminCourseUpdateResponseSchema(BaseModel):
    id: str


class AdminCourseGetRequestSchema(BaseModel):
    id: str


class AdminCourseGetResponseSchema(BaseModel):
    id: str
    title: str
    description: Optional[str]

    level: str
    duration_minutes: int
    language: str
    requires_experience: bool = False

    price: CoursePriceSchema

    category_ids: List[str]
    mentor_ids: List[str]


class AdminCourseDeleteRequestSchema(BaseModel):
    id: str


class AdminCourseDeleteResponseSchema(BaseModel):
    success: bool


class AdminCourseListResponseSchema(BaseModel):
    items: List[AdminCourseGetResponseSchema]
