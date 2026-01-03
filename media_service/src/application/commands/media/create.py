from src.application.commands.media.dto import CreateMediaDTO
from src.domain.repositories.media_repository import IMediaRepository


class CreateMediaCommand:
    def __init__(self, repo: IMediaRepository):
        self.repo = repo

    async def execute(self, dto: CreateMediaDTO):
        return await self.repo.create(
            kind=dto.kind,
            usage=dto.usage,
            original_url=dto.original_url,
            metadata=dto.metadata,
        )
