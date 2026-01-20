from pydantic import BaseModel
from typing import List, Optional


class ModuleGetResponseSchema(BaseModel):
    id: str
    course_id: str
    title: str
    description: Optional[str]
    order_number: int = 0


class ModuleListItemSchema(BaseModel):
    id: str
    course_id: str
    title: str
    description: Optional[str]
    order_number: int = 0
    lessons_count: int = 0
    files_count: int = 0
    duration_minutes: Optional[int] = 0
    has_free_lessons: bool = False


class ModuleListResponseSchema(BaseModel):
    items: List[ModuleListItemSchema]


