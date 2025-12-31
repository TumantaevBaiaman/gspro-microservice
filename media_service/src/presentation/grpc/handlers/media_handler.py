import grpc

from generated.media import media_pb2 as pb2
from generated.media import media_pb2_grpc as pb2_grpc

from src.application.commands.media.dto import CreateMediaDTO, AttachMediaDTO
from src.application.services.media_service import MediaService
from src.domain.enums.media import OwnerService, MediaKind, MediaUsage


class MediaHandler(pb2_grpc.MediaServiceServicer):

    def __init__(self, service: MediaService):
        self.service = service

    async def CreateMedia(self, request, context):
        dto = CreateMediaDTO(
            kind=MediaKind(request.kind),
            usage=MediaUsage(request.usage) if request.usage else None,
            original_url=request.original_url,
            metadata=dict(request.metadata) if request.metadata else None,
        )

        media = await self.service.create.execute(dto)

        return pb2.CreateMediaResponse(
            media=self._map_media(media)
        )

    async def AttachMedia(self, request, context):
        dto = AttachMediaDTO(
            media_id=request.media_id,
            owner_service=OwnerService(request.owner_service),
            owner_id=request.owner_id,
        )

        media = await self.service.attach.execute(dto)

        if not media:
            await context.abort(
                grpc.StatusCode.NOT_FOUND,
                "Media not found",
            )

        return pb2.AttachMediaResponse(
            media=self._map_media(media)
        )

    async def GetMedia(self, request, context):
        media = await self.service.get.execute(
            media_id=request.media_id
        )

        if not media:
            await context.abort(
                grpc.StatusCode.NOT_FOUND,
                "Media not found",
            )

        return pb2.GetMediaResponse(
            media=self._map_media(media)
        )

    async def GetMediaBatch(self, request, context):
        items = await self.service.get_batch.execute(
            media_ids=request.media_ids
        )

        return pb2.GetMediaBatchResponse(
            items=[self._map_media(item) for item in items]
        )

    async def ListMediaByOwner(self, request, context):
        items = await self.service.list_by_owner.execute(
            owner_service=OwnerService(request.owner_service),
            owner_id=request.owner_id,
            kind=MediaKind(request.kind) if request.kind else None,
            usage=MediaUsage(request.usage) if request.usage else None,
        )

        return pb2.ListMediaResponse(
            items=[self._map_media(item) for item in items]
        )

    async def DeleteMedia(self, request, context):
        deleted = await self.service.delete.execute(
            media_id=request.media_id
        )

        return pb2.DeleteMediaResponse(
            success=deleted
        )

    @staticmethod
    def _map_media(media):
        return pb2.Media(
            id=str(media.id),
            owner_service=media.owner_service.value if media.owner_service else "",
            owner_id=str(media.owner_id) if media.owner_id else "",
            kind=media.kind.value,
            usage=media.usage.value if media.usage else "",
            original_url=media.original_url,
            metadata=media.metadata or {},
            status=media.status.value,
            created_at=media.created_at.isoformat(),
        )
