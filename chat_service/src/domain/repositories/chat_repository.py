from abc import ABC, abstractmethod
from typing import Optional, Iterable

from src.domain.enums.chat_type_enum import ChatTypeEnum
from src.infrastructure.db.mongo.models import ChatDocument


class IChatRepository(ABC):

    @abstractmethod
    async def get_by_id(
        self,
        chat_id: str,
    ) -> Optional[ChatDocument]:
        ...

    @abstractmethod
    async def get_by_unique_key(
        self,
        unique_key: str,
    ) -> Optional[ChatDocument]:
        ...

    @abstractmethod
    async def create(
        self,
        *,
        type: ChatTypeEnum,
        course_id: str | None,
        unique_key: str,
    ) -> ChatDocument:
        ...

    @abstractmethod
    async def list_by_ids(
        self,
        chat_ids: Iterable[str],
        chat_type: ChatTypeEnum | None = None,
    ) -> list[ChatDocument]:
        ...

    @abstractmethod
    async def list_private_by_course(
            self,
            course_id: str,
    ) -> list[ChatDocument]:
        ...
