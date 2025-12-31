import grpc
from google.protobuf.json_format import MessageToDict

from generated.course import admin_lesson_pb2 as pb2
from generated.course import admin_lesson_pb2_grpc as pb2_grpc

from src.domain.dto.admin_lesson_dto import (
    AdminLessonCreateDTO,
    AdminLessonUpdateDTO,
)
from src.domain.exceptions.admin_lesson import LessonNotFoundError
from src.application.services.admin_lesson_service import AdminLessonService


class AdminLessonHandler(pb2_grpc.AdminLessonServiceServicer):

    def __init__(self, service: AdminLessonService):
        self.service = service

    async def AdminCreateLesson(self, request, context):
        data = MessageToDict(
            request,
            preserving_proto_field_name=True
        )
        dto = AdminLessonCreateDTO(**data)

        lesson = await self.service.create.execute(dto)

        return pb2.AdminCreateLessonResponse(
            id=str(lesson.id)
        )

    async def AdminGetLesson(self, request, context):
        try:
            lesson = await self.service.get.execute(request.id)
            return pb2.AdminGetLessonResponse(
                id=str(lesson.id),
                module_id=lesson.module_id,
                title=lesson.title,

                type=lesson.type.value,
                access_type=lesson.access_type.value,

                content=lesson.content or "",
                video_id=lesson.video_id or "",

                duration=lesson.duration or "",
                order_number=lesson.order_number or 0,
                is_active=lesson.is_active,
            )

        except LessonNotFoundError as e:
            await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

    async def AdminUpdateLesson(self, request, context):
        dto = AdminLessonUpdateDTO(**MessageToDict(request))

        try:
            lesson = await self.service.update.execute(
                lesson_id=request.id,
                dto=dto,
            )

            return pb2.AdminUpdateLessonResponse(
                id=str(lesson.id)
            )

        except LessonNotFoundError as e:
            await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

    async def AdminDeleteLesson(self, request, context):
        try:
            await self.service.delete.execute(request.id)

            return pb2.AdminDeleteLessonResponse(
                success=True
            )

        except LessonNotFoundError as e:
            await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

    async def AdminListLessons(self, request, context):
        lessons = await self.service.list.execute(
            module_id=request.module_id or None
        )

        response = pb2.AdminListLessonsResponse()

        for lesson in lessons:
            response.items.add(
                id=str(lesson.id),
                module_id=lesson.module_id,
                title=lesson.title,
                type=lesson.type.value,
                order_number=lesson.order_number or 0,
                is_active=lesson.is_active,
            )

        return response
