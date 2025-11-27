import grpc

from generated.course import course_pb2 as pb2
from generated.course import course_pb2_grpc as pb2_grpc

from app.application.services.course_service import CourseService


class CourseHandler(pb2_grpc.CourseServiceServicer):

    async def CreateCourse(self, request, context):
        service = CourseService()

        course = await service.create_course(
            title=request.title,
            description=request.description
        )

        return pb2.CreateCourseResponse(id=str(course.id))

    async def GetCourse(self, request, context):
        service = CourseService()

        course = await service.get_course_by_id(
            course_id=request.id
        )

        if not course:
            await context.abort(
                grpc.StatusCode.NOT_FOUND,
                f"Course with ID {request.id} not found."
            )

        return pb2.GetCourseByIdResponse(
            id=str(course.id),
            title=course.title,
            description=course.description or ""
        )
