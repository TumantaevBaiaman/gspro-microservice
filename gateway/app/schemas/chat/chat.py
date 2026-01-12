from typing import Optional, List

from pydantic import BaseModel


class GetOrCreateChatRequest(BaseModel):
    chat_type: str  # DIRECT | COURSE_PRIVATE | COURSE_GROUP

    peer_id: str | None = None

    course_id: str | None = None
    student_id: str | None = None


class GetOrCreateChatResponse(BaseModel):
    chat_id: str
    chat_type: str


class ChatAttachmentResponse(BaseModel):
    file_id: str
    url: str
    filename: Optional[str] = None
    mime_type: Optional[str] = None
    size: Optional[int] = None
    duration: Optional[int] = None


class ChatMessageResponse(BaseModel):
    id: str
    chat_id: str
    sender_id: str
    type: str
    text: Optional[str]
    attachments: List[ChatAttachmentResponse]
    created_at: str


class ChatMessageListResponse(BaseModel):
    messages: List[ChatMessageResponse]