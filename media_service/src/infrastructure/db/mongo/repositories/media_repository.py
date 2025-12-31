from uuid import UUID
from typing import Iterable

from beanie import PydanticObjectId
from beanie.odm.operators.find.comparison import In
from bson import ObjectId

from src.domain.repositories.media_repository import IMediaRepository
from src.infrastructure.db.mongo.models.media_asset_document import (
    MediaAssetDocument,
    MediaStatus,
)
from src.domain.enums.media import OwnerService, MediaKind, MediaUsage


class MediaRepository(IMediaRepository):

    async def create(
        self,
        *,
        kind: MediaKind,
        usage: MediaUsage | None,
        original_url: str,
        metadata: dict | None,
    ) -> MediaAssetDocument:
        doc = MediaAssetDocument(
            kind=kind,
            usage=usage,
            original_url=original_url,
            metadata=metadata,
            status=MediaStatus.draft,
        )
        await doc.insert()
        return doc

    async def attach(
        self,
        *,
        media_id: str,
        owner_service: OwnerService,
        owner_id: str,
    ) -> MediaAssetDocument | None:
        doc = await MediaAssetDocument.get(
            media_id
        )

        if not doc:
            return None

        doc.owner_service = owner_service
        doc.owner_id = owner_id
        doc.status = MediaStatus.attached

        await doc.save()
        return doc

    async def get_by_id(
        self,
        *,
        media_id: UUID,
    ) -> MediaAssetDocument | None:
        return await MediaAssetDocument.get(
            media_id
        )

    async def list_by_owner(
        self,
        *,
        owner_service: OwnerService,
        owner_id: UUID,
        kind: MediaKind | None = None,
        usage: MediaUsage | None = None,
    ) -> list[MediaAssetDocument]:
        filters = [
            MediaAssetDocument.owner_service == owner_service,
            MediaAssetDocument.owner_id == owner_id,
            MediaAssetDocument.status == MediaStatus.attached,
            MediaAssetDocument.is_active == True,
        ]

        if kind:
            filters.append(MediaAssetDocument.kind == kind)

        if usage:
            filters.append(MediaAssetDocument.usage == usage)

        return await MediaAssetDocument.find(*filters).to_list()

    async def get_batch(
            self,
            *,
            media_ids,
    ):
        ids = [ObjectId(str(i)) for i in media_ids]

        return await MediaAssetDocument.find(
            {"_id": {"$in": ids}}
        ).to_list()

    async def soft_delete(
        self,
        *,
        media_id: UUID,
    ) -> bool:
        doc = await MediaAssetDocument.find_one(
            MediaAssetDocument.id == media_id,
            MediaAssetDocument.is_active == True,
        )

        if not doc:
            return False

        doc.is_active = False
        await doc.save()
        return True
