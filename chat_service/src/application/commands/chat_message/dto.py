from typing import Optional, List
from dataclasses import dataclass

from src.domain.enums.chat_scope_enum import ChatScopeEnum
from src.infrastructure.db.mongo.models.chat_document import ChatParticipant
from src.infrastructure.db.mongo.models.chat_message_document import (
    ChatMessagePayload,
    ChatMessageContext,
)


@dataclass(slots=True)
class SendMessageDTO:
    scope: ChatScopeEnum
    sender_id: str
    participants: List[ChatParticipant]
    payload: ChatMessagePayload

    course_id: Optional[str] = None
    context: Optional[ChatMessageContext] = None
