import grpc

from generated.course import course_pb2 as pb2
from generated.course import course_pb2_grpc as pb2_grpc

from google.protobuf.json_format import MessageToDict

from src.domain.dto import course_dto
from src.application.services.course_service import CourseService


class CourseHandler(pb2_grpc.CourseServiceServicer):

    def __init__(self):
        self.service = CourseService()

    async def CreateCourse(self, request, context):

        dto = course_dto.CourseCreateDTO(**MessageToDict(request))

        course = await self.service.create_course(dto)

        return pb2.CreateCourseResponse(id=str(course.id))

    async def GetCourse(self, request, context):

        course = await self.service.get_course_by_id(
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
