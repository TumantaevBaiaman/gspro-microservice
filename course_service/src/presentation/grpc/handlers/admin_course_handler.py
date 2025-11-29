import grpc
from fastapi import HTTPException

from generated.course import admin_course_pb2 as pb2
from generated.course import admin_course_pb2_grpc as pb2_grpc

from google.protobuf.json_format import MessageToDict

from src.domain.dto import admin_course_dto
from src.application.services.admin_course_service import AdminCourseService


class AdminCourseHandler(pb2_grpc.AdminCourseServiceServicer):

    def __init__(self):
        self.service = AdminCourseService()

    async def AdminCreateCourse(self, request, context):
        dto = admin_course_dto.AdminCourseCreateDTO(**MessageToDict(request))
        try:
            course = await self.service.create_course(dto=dto)
            return pb2.AdminCreateCourseResponse(id=str(course.id))
        except HTTPException as e:
            if e.status_code == 409:
                await context.abort(grpc.StatusCode.ALREADY_EXISTS, e.detail)

    async def AdminUpdateCourse(self, request, context):
        dto = admin_course_dto.AdminCourseUpdateDTO(**MessageToDict(request))
        try:
            course = await self.service.update_course(course_id=request.id, dto=dto)
            return pb2.AdminUpdateCourseResponse(id=str(course.id))
        except HTTPException as e:
            if e.status_code == 404:
                return context.abort(grpc.StatusCode.NOT_FOUND, e.detail)
            if e.status_code == 409:
                return context.abort(grpc.StatusCode.ALREADY_EXISTS, e.detail)

    async def AdminGetCourse(self, request, context):
        try:
            course = await self.service.get_course(request.id)
            return pb2.AdminGetCourseResponse(
                id=str(course.id),
                title=course.title,
                description=course.description or "",
                preview_url=course.preview_url or "",
                mentor_id=course.mentor_id or "",
                category_id=course.category_id or "",
            )
        except HTTPException as e:
            if e.status_code == 404:
                await context.abort(grpc.StatusCode.NOT_FOUND, e.detail)

    async def AdminDeleteCourse(self, request, context):
        try:
            await self.service.delete_course(request.id)
            return pb2.AdminDeleteCourseResponse(success=True)
        except HTTPException as e:
            if e.status_code == 404:
                await context.abort(grpc.StatusCode.NOT_FOUND, e.detail)

    async def AdminListCourses(self, request, context):
        courses = await self.service.list_courses()
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
