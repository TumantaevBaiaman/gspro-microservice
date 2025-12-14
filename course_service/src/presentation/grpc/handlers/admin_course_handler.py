import grpc
from google.protobuf.json_format import MessageToDict

from generated.course import admin_course_pb2 as pb2
from generated.course import admin_course_pb2_grpc as pb2_grpc

from src.domain.dto import admin_course_dto
from src.domain.exceptions.admin_course import (
    CourseNotFoundError,
    CourseAlreadyExistsError,
)
from src.application.services.admin_course_service import AdminCourseService


class AdminCourseHandler(pb2_grpc.AdminCourseServiceServicer):

    def __init__(self, service: AdminCourseService):
        self.service = service

    async def AdminCreateCourse(self, request, context):
        dto = admin_course_dto.AdminCourseCreateDTO(**MessageToDict(request, preserving_proto_field_name=True))

        try:
            course = await self.service.create.execute(dto)
            return pb2.AdminCreateCourseResponse(id=str(course.id))

        except CourseAlreadyExistsError as e:
            await context.abort(grpc.StatusCode.ALREADY_EXISTS, str(e))

    async def AdminUpdateCourse(self, request, context):
        raw = MessageToDict(
            request,
            preserving_proto_field_name=True
        )

        data = {
            k: v
            for k, v in raw.items()
            if k != "id" and v not in ("", None)
        }

        dto = admin_course_dto.AdminCourseUpdateDTO(**data)

        try:
            course = await self.service.update.execute(
                course_id=request.id,
                dto=dto,
            )
            return pb2.AdminUpdateCourseResponse(id=str(course.id))

        except CourseNotFoundError as e:
            await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

        except CourseAlreadyExistsError as e:
            await context.abort(grpc.StatusCode.ALREADY_EXISTS, str(e))

    async def AdminGetCourse(self, request, context):
        try:
            course = await self.service.get.execute(request.id)

            return pb2.AdminGetCourseResponse(
                id=str(course.id),
                title=course.title,
                description=course.description or "",
                preview_url=course.preview_url or "",
                mentor_id=course.mentor_id or "",
                category_id=course.category_id or "",
            )

        except CourseNotFoundError as e:
            await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

    async def AdminDeleteCourse(self, request, context):
        try:
            await self.service.delete.execute(request.id)
            return pb2.AdminDeleteCourseResponse(success=True)

        except CourseNotFoundError as e:
            await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

    async def AdminListCourses(self, request, context):
        courses = await self.service.list.execute()
        response = pb2.AdminListCoursesResponse()

        for course in courses:
            response.items.add(
                id=str(course.id),
                title=course.title,
                description=course.description or "",
                preview_url=course.preview_url or "",
                mentor_id=course.mentor_id or "",
                category_id=course.category_id or "",
            )

        return response
