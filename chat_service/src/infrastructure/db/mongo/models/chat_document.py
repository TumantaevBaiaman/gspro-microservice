from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from src.domain.enums.chat_message_type_enum import ChatMessageTypeEnum
from src.domain.enums.chat_type_enum import ChatTypeEnum
from .base import BaseDocument


class LastMessagePreview(BaseModel):
    type: ChatMessageTypeEnum
    text: Optional[str] = None
    attachments_count: int = 0


class ChatDocument(BaseDocument):
    type: ChatTypeEnum
    course_id: Optional[str] = None

    unique_key: str

    last_message: Optional[LastMessagePreview] = None
    last_message_sender_id: Optional[str] = None
    last_message_at: Optional[datetime] = None

    is_archived: bool = False

    class Settings:
        name = "chats"
