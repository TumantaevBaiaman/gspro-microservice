from src.application.commands.media.dto import AttachMediaDTO
from src.domain.repositories.media_repository import IMediaRepository


class AttachMediaCommand:
    def __init__(self, repo: IMediaRepository):
        self.repo = repo

    async def execute(self, dto: AttachMediaDTO):
        return await self.repo.attach(
            media_id=dto.media_id,
            owner_service=dto.owner_service,
            owner_id=dto.owner_id,
        )
