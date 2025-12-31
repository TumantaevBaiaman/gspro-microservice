from uuid import UUID
from src.domain.repositories.media_repository import IMediaRepository


class SoftDeleteMediaCommand:
    def __init__(self, repo: IMediaRepository):
        self.repo = repo

    async def execute(self, media_id: UUID) -> bool:
        return await self.repo.soft_delete(media_id=media_id)