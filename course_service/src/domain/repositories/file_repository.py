from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from src.domain.entities.file_entity import FileEntity
from src.domain.enums.file_type import FileType
from src.domain.enums.file_scope import FileScope


class IFileRepository(ABC):

    @abstractmethod
    async def get_by_id(self, file_id: UUID) -> Optional[FileEntity]:
        pass

    @abstractmethod
    async def list_by_scope(
        self,
        *,
        scope: FileScope,
    ) -> list[FileEntity]:
        pass

    @abstractmethod
    async def list_by_scope_and_type(
        self,
        *,
        scope: FileScope,
        file_type: FileType,
    ) -> list[FileEntity]:
        pass

    @abstractmethod
    async def save(self, file: FileEntity) -> FileEntity:
        pass

    @abstractmethod
    async def delete(self, file_id: UUID) -> None:
        pass
