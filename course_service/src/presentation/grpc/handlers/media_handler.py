import grpc

from generated.course import media_pb2 as pb2
from generated.course import media_pb2_grpc as pb2_grpc

from src.application.services.media_service import MediaService
from src.domain.dto.image_dto import UploadImageDTO
from src.domain.dto.file_dto import UploadFileDTO
from src.domain.exceptions.media import MediaError


class MediaHandler(pb2_grpc.CourseMediaServiceServicer):

    def __init__(self, service: MediaService):
        self.service = service

    async def UploadImage(self, request, context):
        try:
            image = await self.service.upload_image.execute(
                UploadImageDTO(
                    type=request.type,
                    original_url=request.original_url,
                    thumb_small_url=request.thumb_small_url or None,
                    thumb_medium_url=request.thumb_medium_url or None,
                )
            )

            return pb2.UploadImageResponse(id=str(image.id))

        except MediaError as e:
            await context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))

    async def UploadFile(self, request, context):
        try:
            file = await self.service.upload_file.execute(
                UploadFileDTO(
                    type=request.type,
                    scope=request.scope,
                    path=request.path,
                    filename=request.filename,
                    mime_type=request.mime_type,
                    size_bytes=request.size_bytes,
                )
            )

            return pb2.UploadFileResponse(id=str(file.id))

        except MediaError as e:
            await context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))

