from abc import ABC, abstractmethod
from datetime import datetime

from src.domain.enums.chat_participant_role_enum import ChatParticipantRole
from src.infrastructure.db.mongo.models import ChatParticipantDocument


class IChatParticipantRepository(ABC):

    @abstractmethod
    async def add_participant(
        self,
        *,
        chat_id: str,
        user_id: str,
        role: ChatParticipantRole,
    ) -> None:
        ...

    @abstractmethod
    async def exists(
        self,
        *,
        chat_id: str,
        user_id: str,
    ) -> bool:
        ...

    @abstractmethod
    async def list_by_chat(
        self,
        *,
        chat_id: str,
    ) -> list[ChatParticipantDocument]:
        ...

    @abstractmethod
    async def list_chat_ids_by_user(
        self,
        *,
        user_id: str,
    ) -> list[str]:
        ...

    @abstractmethod
    async def update_last_read(
        self,
        *,
        chat_id: str,
        user_id: str,
        last_read_at: datetime,
    ) -> None:
        ...

    @abstractmethod
    async def set_muted(
        self,
        *,
        chat_id: str,
        user_id: str,
        value: bool,
    ) -> None:
        ...

    @abstractmethod
    async def set_archived(
        self,
        *,
        chat_id: str,
        user_id: str,
        value: bool,
    ) -> None:
        ...

    @abstractmethod
    async def list_by_user(
            self,
            *,
            user_id: str,
            limit: int | None = None,
            offset: int | None = None,
    ) -> tuple[list[ChatParticipantDocument], int]:
        ...

    @abstractmethod
    async def list_by_chat_ids(
            self,
            *,
            chat_ids: list[str],
    ) -> list[ChatParticipantDocument]:
        ...
