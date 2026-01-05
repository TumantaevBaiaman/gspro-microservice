from pydantic import BaseModel
from typing import List, Optional


class ModuleGetResponseSchema(BaseModel):
    id: str
    course_id: str
    title: str
    description: Optional[str]
    order_number: int


class ModuleListItemSchema(BaseModel):
    id: str
    course_id: str
    title: str
    description: Optional[str]
    order_number: int
    lessons_count: int = 0


class ModuleListResponseSchema(BaseModel):
    items: List[ModuleListItemSchema]


