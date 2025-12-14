from typing import Optional

from pydantic import BaseModel


class AdminCourseCreateRequestSchema(BaseModel):
    title: str
    description: Optional[str]
    preview_url: Optional[str] = None
    mentor_id: Optional[str] = None
    category_id: Optional[str] = None


class AdminCourseCreateResponseSchema(BaseModel):
    id: str


class AdminCourseUpdateRequestSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    preview_url: Optional[str] = None
    mentor_id: Optional[str] = None
    category_id: Optional[str] = None


class AdminCourseUpdateResponseSchema(BaseModel):
    id: str


class AdminCourseDeleteRequestSchema(BaseModel):
    id: str


class AdminCourseDeleteResponseSchema(BaseModel):
    success: bool


class AdminCourseGetRequestSchema(BaseModel):
    id: str


class AdminCourseGetResponseSchema(BaseModel):
    id: str
    title: str
    description: Optional[str]
    preview_url: Optional[str] = None
    mentor_id: Optional[str] = None
    category_id: Optional[str] = None

