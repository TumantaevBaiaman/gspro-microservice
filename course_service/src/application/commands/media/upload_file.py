from src.domain.entities.file_entity import FileEntity
from src.domain.dto.file_dto import UploadFileDTO
from src.domain.repositories.file_repository import IFileRepository


class UploadFileCommand:
    def __init__(self, repo: IFileRepository):
        self.repo = repo

    async def execute(self, dto: UploadFileDTO) -> FileEntity:
        file = FileEntity(
            type=dto.type,
            scope=dto.scope,
            path=dto.path,
            filename=dto.filename,
            mime_type=dto.mime_type,
            size_bytes=dto.size_bytes,
        )

        return await self.repo.save(file)
