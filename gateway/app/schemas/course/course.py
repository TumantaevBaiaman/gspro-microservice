from typing import Optional

from pydantic import BaseModel, Field


class CourseGetRequestSchema(BaseModel):
    id: str


class CourseGetResponseSchema(BaseModel):
    id: str
    title: str
    description: Optional[str]
    preview_url: Optional[str] = None
    mentor_id: Optional[str] = None
    category_id: Optional[str] = None


class CourseListItemSchema(BaseModel):
    id: str
    title: str
    preview_url: str | None = None
    mentor_id: str | None = None
    category_id: str | None = None


class CourseListResponseSchema(BaseModel):
    items: list[CourseListItemSchema]
    total: int = Field(..., example=120)