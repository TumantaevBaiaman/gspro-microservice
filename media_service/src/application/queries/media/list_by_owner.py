from uuid import UUID

from src.domain.enums.media import OwnerService, MediaKind, MediaUsage
from src.domain.repositories.media_repository import IMediaRepository


class ListMediaByOwnerQuery:
    def __init__(self, repo: IMediaRepository):
        self.repo = repo

    async def execute(
        self,
        *,
        owner_service: OwnerService,
        owner_id: UUID,
        kind: MediaKind | None = None,
        usage: MediaUsage | None = None,
    ):
        return await self.repo.list_by_owner(
            owner_service=owner_service,
            owner_id=owner_id,
            kind=kind,
            usage=usage,
        )