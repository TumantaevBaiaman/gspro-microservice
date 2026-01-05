from src.application.commands.media.dto import CreateAndAttachMediaDTO
from src.domain.repositories.media_repository import IMediaRepository


class CreateAndAttachMediaCommand:
    def __init__(self, repo: IMediaRepository):
        self.repo = repo

    async def execute(self, dto: CreateAndAttachMediaDTO):
        return await self.repo.create_and_attach(
            kind=dto.kind,
            usage=dto.usage,
            original_url=dto.original_url,
            metadata=dto.metadata,
            owner_service=dto.owner_service,
            owner_id=dto.owner_id,
        )
