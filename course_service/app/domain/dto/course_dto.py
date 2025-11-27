from pydantic import BaseModel
from typing import Optional


class CourseCreateDTO(BaseModel):
    title: str
    description: Optional[str] = None
    preview_url: Optional[str] = None
    mentor_id: Optional[int] = None
    category_id: Optional[str] = None
