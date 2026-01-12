from typing import Optional, List
from pydantic import BaseModel, Field


class AdminLessonCreateRequestSchema(BaseModel):
    module_id: str
    title: str

    type: str = Field(default="TEXT")
    access_type: str = Field(default="PAID")
    content: Optional[str] = None

    video_id: Optional[str] = None
    duration: Optional[str] = None

    order_number: Optional[int] = None
    is_active: bool = True

    file_ids: List[str] = []


class AdminLessonCreateResponseSchema(BaseModel):
    id: str


class AdminLessonGetRequestSchema(BaseModel):
    id: str


class AdminLessonGetResponseSchema(BaseModel):
    id: str
    module_id: str
    title: str

    type: str
    access_type: str

    content: Optional[str] = None
    video_id: Optional[str] = None
    duration: Optional[str] = None

    order_number: int = 0
    is_active: bool = True


class AdminLessonUpdateRequestSchema(BaseModel):
    id: str

    module_id: Optional[str] = None
    title: Optional[str] = None

    type: Optional[str] = None
    access_type: Optional[str] = None

    content: Optional[str] = None
    video_id: Optional[str] = None
    duration: Optional[str] = None

    order_number: Optional[int] = None
    is_active: Optional[bool] = None


class AdminLessonUpdateResponseSchema(BaseModel):
    id: str


class AdminLessonDeleteRequestSchema(BaseModel):
    id: str


class AdminLessonDeleteResponseSchema(BaseModel):
    success: bool


class AdminLessonListRequestSchema(BaseModel):
    module_id: Optional[str] = None


class AdminLessonListResponseSchema(BaseModel):
    items: List[AdminLessonGetResponseSchema]
