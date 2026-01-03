from abc import ABC, abstractmethod
from uuid import UUID
from typing import Iterable

from src.infrastructure.db.mongo.models.media_asset_document import MediaAssetDocument
from src.domain.enums.media import OwnerService, MediaKind, MediaUsage


class IMediaRepository(ABC):

    @abstractmethod
    async def create(
        self,
        *,
        kind: MediaKind,
        usage: MediaUsage | None,
        original_url: str,
        metadata: dict | None,
    ) -> MediaAssetDocument:
        ...

    @abstractmethod
    async def attach(
        self,
        *,
        media_id: str,
        owner_service: OwnerService,
        owner_id: str,
    ) -> MediaAssetDocument | None:
        ...

    @abstractmethod
    async def get_by_id(
        self,
        *,
        media_id: str,
    ) -> MediaAssetDocument | None:
        ...

    @abstractmethod
    async def list_by_owner(
        self,
        *,
        owner_service: OwnerService,
        owner_id: str,
        kind: MediaKind | None = None,
        usage: MediaUsage | None = None,
    ) -> list[MediaAssetDocument]:
        ...

    @abstractmethod
    async def get_batch(
        self,
        *,
        media_ids: Iterable[UUID],
    ) -> list[MediaAssetDocument]:
        ...

    @abstractmethod
    async def soft_delete(
        self,
        *,
        media_id: UUID,
    ) -> bool:
        ...
