from pydantic import BaseModel
from typing import Optional


class AdminCourseCreateDTO(BaseModel):
    title: str
    description: Optional[str] = None
    preview_url: Optional[str] = None
    mentor_id: Optional[str] = None
    category_id: Optional[str] = None


class AdminCourseUpdateDTO(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    preview_url: Optional[str] = None
    mentor_id: Optional[str] = None
    category_id: Optional[str] = None
