from typing import Optional

from beanie import Indexed
from datetime import datetime

from pydantic import Field

from src.domain.enums.chat_participant_role_enum import ChatParticipantRole
from .base import BaseDocument

class ChatParticipantDocument(BaseDocument):
    chat_id: str = Indexed()
    user_id: str = Indexed()

    role: ChatParticipantRole
    joined_at: datetime = Field(default_factory=datetime.utcnow)

    is_muted: bool = False
    is_archived: bool = False
    last_read_at: Optional[datetime] = None

    class Settings:
        name = "chat_participants"
        indexes = [
            [("chat_id", 1), ("user_id", 1)],
        ]
