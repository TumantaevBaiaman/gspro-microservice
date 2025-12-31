from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from src.domain.enums.chat_scope_enum import ChatScopeEnum
from src.infrastructure.db.mongo.models.chat_document import ChatDocument, ChatParticipant
from src.infrastructure.db.mongo.models.chat_message_document import (
    ChatMessageDocument,
    ChatMessagePayload,
    ChatMessageContext,
)


class IChatMessageRepository(ABC):

    @abstractmethod
    async def send_message(
        self,
        *,
        scope: ChatScopeEnum,
        sender_id: str,
        participants: List[ChatParticipant],
        payload: ChatMessagePayload,
        course_id: Optional[str] = None,
        context: Optional[ChatMessageContext] = None,
    ) -> Tuple[ChatDocument, ChatMessageDocument]:
        ...

    @abstractmethod
    async def list_messages(
        self,
        *,
        chat_id: str,
        limit: int,
        offset: int,
    ) -> Tuple[List[ChatMessageDocument], int]:
        ...
