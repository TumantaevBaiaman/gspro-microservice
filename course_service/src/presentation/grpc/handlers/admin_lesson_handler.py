import grpc
from fastapi import HTTPException
from google.protobuf.json_format import MessageToDict

from generated.course import admin_lesson_pb2 as pb2
from generated.course import admin_lesson_pb2_grpc as pb2_grpc

from src.domain.dto.admin_lesson_dto import AdminLessonCreateDTO, AdminLessonUpdateDTO
from src.application.services.admin_lesson_service import AdminLessonService


class AdminLessonHandler(pb2_grpc.AdminLessonServiceServicer):

    def __init__(self, service: AdminLessonService):
        self.service = service

    async def AdminCreateLesson(self, request, context):
        dto = AdminLessonCreateDTO(**MessageToDict(request))
        lesson = await self.service.create_lesson(dto)
        return pb2.AdminCreateLessonResponse(id=str(lesson.id))

    async def AdminGetLesson(self, request, context):
        try:
            lesson = await self.service.get_lesson(request.id)
            return pb2.AdminGetLessonResponse(
                id=str(lesson.id),
                module_id=lesson.module_id,
                title=lesson.title,
                type=lesson.type.value,
                content=lesson.content or "",
                video_url=lesson.video_url or "",
                duration=lesson.duration or "",
                order_number=lesson.order_number or 0,
                is_active=lesson.is_active,
            )
        except HTTPException as e:
            if e.status_code == 404:
                await context.abort(grpc.StatusCode.NOT_FOUND, e.detail)

    async def AdminUpdateLesson(self, request, context):
        dto = AdminLessonUpdateDTO(**MessageToDict(request))
        try:
            lesson = await self.service.update_lesson(request.id, dto)
            return pb2.AdminUpdateLessonResponse(id=str(lesson.id))
        except HTTPException as e:
            if e.status_code == 404:
                await context.abort(grpc.StatusCode.NOT_FOUND, e.detail)

    async def AdminDeleteLesson(self, request, context):
        try:
            await self.service.delete_lesson(request.id)
            return pb2.AdminDeleteLessonResponse(success=True)
        except HTTPException as e:
            if e.status_code == 404:
                await context.abort(grpc.StatusCode.NOT_FOUND, e.detail)

    async def AdminListLessons(self, request, context):
        lessons = await self.service.list_lessons(request.module_id or None)

        response = pb2.AdminListLessonsResponse()
        for l in lessons:
            response.items.add(
                id=str(l.id),
                module_id=l.module_id,
                title=l.title,
                type=l.type.value,
                order_number=l.order_number or 0,
                is_active=l.is_active,
            )
        return response
