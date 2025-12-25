from uuid import UUID
from typing import Optional

from src.domain.entities.file_entity import FileEntity
from src.domain.enums.file_type import FileType
from src.domain.enums.file_scope import FileScope
from src.domain.repositories.file_repository import IFileRepository


class FileRepository(IFileRepository):

    async def get_by_id(self, file_id: UUID) -> Optional[FileEntity]:
        return await FileEntity.get(file_id)

    async def list_by_scope(
        self,
        *,
        scope: FileScope,
    ) -> list[FileEntity]:
        return await (
            FileEntity.find(
                FileEntity.scope == scope,
            )
            .to_list()
        )

    async def list_by_scope_and_type(
        self,
        *,
        scope: FileScope,
        file_type: FileType,
    ) -> list[FileEntity]:
        return await (
            FileEntity.find(
                FileEntity.scope == scope,
                FileEntity.type == file_type,
            )
            .to_list()
        )

    async def save(self, file: FileEntity) -> FileEntity:
        await file.save()
        return file

    async def delete(self, file_id: UUID) -> None:
        file = await FileEntity.get(file_id)
        if file:
            await file.delete()
