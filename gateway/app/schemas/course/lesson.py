from pydantic import BaseModel
from typing import List, Optional


class LessonShortSchema(BaseModel):
    id: str
    title: str

    type: str
    access_type: str
    duration: Optional[str]

    order_number: int = 0


class LessonListResponse(BaseModel):
    items: List[LessonShortSchema]


class LessonSchema(BaseModel):
    id: str
    module_id: str
    title: str

    type: str
    content: Optional[str]

    duration: Optional[str]

    order_number: int = 0

    access_type: str


class LessonStreamResponse(BaseModel):
    embed_url: str
    expires_at: int