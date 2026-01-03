from uuid import UUID
from typing import Any
from pydantic import Field

from src.domain.enums.media import *
from .base import BaseDocument


class MediaAssetDocument(BaseDocument):
    owner_service: OwnerService | None = Field(
        None, description="Who owns this media asset"
    )
    owner_id: str | None = Field(
        None, description="ID of the owner entity"
    )

    kind: MediaKind = Field(..., description="Type of media asset")
    usage: MediaUsage | None = Field(None, description="Intended usage of the media asset")

    original_url: str = Field(..., description="URL to the original media file")

    metadata: dict[str, Any] | None = Field(
        default=None,
        description="Kind-specific metadata (thumbs, duration, etc)",
    )

    status: MediaStatus = Field(
        default=MediaStatus.draft,
        description="Media lifecycle status",
    )

    class Settings:
        name = "media_assets"
        indexes = [
            ("owner_service", "owner_id"),
            "kind",
            "usage",
        ]
