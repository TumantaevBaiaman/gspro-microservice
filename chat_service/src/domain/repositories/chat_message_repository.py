from abc import ABC, abstractmethod
from typing import Iterable

from src.infrastructure.db.mongo.models.chat_message_document import ChatMessagePayload, ChatMessageContext, \
    ChatMessageDocument


class IChatMessageRepository(ABC):

    @abstractmethod
    async def create(
        self,
        *,
        chat_id: str,
        sender_id: str,
        payload: ChatMessagePayload,
        context: ChatMessageContext,
    ) -> ChatMessageDocument:
        ...

    @abstractmethod
    async def get_by_id(
        self,
        message_id: str,
    ) -> ChatMessageDocument | None:
        ...

    @abstractmethod
    async def list_by_chat(
        self,
        *,
        chat_id: str,
        limit: int = 50,
        offset: int = 0,
    ) -> list[ChatMessageDocument]:
        ...

    @abstractmethod
    async def list_by_reference(
        self,
        *,
        chat_id: str,
        reference_type: str,
        reference_id: str,
        limit: int = 50,
        offset: int = 0,
    ) -> list[ChatMessageDocument]:
        ...

    @abstractmethod
    async def update_text(
        self,
        *,
        message_id: str,
        new_text: str,
    ) -> None:
        ...

    @abstractmethod
    async def soft_delete(
        self,
        *,
        message_id: str,
    ) -> None:
        ...
