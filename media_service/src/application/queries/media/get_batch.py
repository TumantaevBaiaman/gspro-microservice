from uuid import UUID
from typing import Iterable

from src.domain.repositories.media_repository import IMediaRepository


class GetMediaBatchQuery:
    def __init__(self, repo: IMediaRepository):
        self.repo = repo

    async def execute(
        self,
        *,
        media_ids: Iterable[UUID],
    ):
        return await self.repo.get_batch(media_ids=media_ids)