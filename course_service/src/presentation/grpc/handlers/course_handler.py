import grpc

from generated.course import course_pb2 as pb2
from generated.course import course_pb2_grpc as pb2_grpc

from src.application.services.course_service import CourseService
from src.domain.exceptions.course import CourseNotFoundError


class CourseHandler(pb2_grpc.CourseServiceServicer):

    def __init__(self, service: CourseService):
        self.service = service

    async def GetCourse(self, request, context):
        try:
            course = await self.service.get.execute(request.id)

            return pb2.GetCourseResponse(
                id=str(course.id),
                title=course.title,
                description=course.description or "",
                preview_url=course.preview_url or "",
                mentor_id=course.mentor_id,
                category_id=course.category_id,
            )

        except CourseNotFoundError as e:
            await context.abort(
                grpc.StatusCode.NOT_FOUND,
                str(e)
            )

    async def ListCourses(self, request, context):
        limit = request.limit or 10
        offset = request.offset or 0

        items, total = await self.service.list.execute(
            limit=limit,
            offset=offset
        )

        return pb2.ListCoursesResponse(
            items=[
                pb2.Course(
                    id=str(course.id),
                    title=course.title,
                    description=course.description or "",
                    preview_url=course.preview_url or "",
                    mentor_id=course.mentor_id,
                    category_id=course.category_id,
                )
                for course in items
            ],
            total=total
        )
