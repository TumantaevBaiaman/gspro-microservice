from uuid import UUID

from pydantic import BaseModel
from src.domain.enums.media import MediaKind, MediaUsage, OwnerService


class CreateMediaDTO(BaseModel):
    kind: MediaKind
    usage: MediaUsage | None = None

    original_url: str
    metadata: dict | None = None


class AttachMediaDTO(BaseModel):
    media_id: str
    owner_service: OwnerService
    owner_id: str