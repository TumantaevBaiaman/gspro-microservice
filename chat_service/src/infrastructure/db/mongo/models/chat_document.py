from datetime import datetime
from typing import Optional

from src.domain.enums.chat_type_enum import ChatTypeEnum
from .base import BaseDocument


class ChatDocument(BaseDocument):
    type: ChatTypeEnum
    course_id: Optional[str] = None

    unique_key: str

    last_message_at: Optional[datetime] = None
    is_archived: bool = False

    class Settings:
        name = "chats"
