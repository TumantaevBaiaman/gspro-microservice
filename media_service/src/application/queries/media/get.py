from uuid import UUID
from src.domain.repositories.media_repository import IMediaRepository


class GetMediaQuery:
    def __init__(self, repo: IMediaRepository):
        self.repo = repo

    async def execute(self, media_id: UUID):
        return await self.repo.get_by_id(media_id=media_id)