import grpc

from generated.subscription import course_access_pb2 as pb2
from generated.subscription import course_access_pb2_grpc as pb2_grpc

from src.application.services import (
    CourseAccessService,
)
from src.application.commands.course_access.dto import (
    GrantCourseAccessDTO,
    RevokeCourseAccessDTO,
)
from src.application.queries.course_access.dto import (
    CheckCourseAccessDTO,
)


class CourseAccessHandler(
    pb2_grpc.CourseAccessServiceServicer
):
    def __init__(self, service: CourseAccessService):
        self.service = service

    async def GrantAccess(self, request, context):
        dto = GrantCourseAccessDTO(
            user_id=request.user_id,
            course_id=request.course_id,
        )

        try:
            await self.service.grant.execute(dto)
        except Exception as e:
            await context.abort(
                grpc.StatusCode.INTERNAL,
                str(e),
            )

        return pb2.GrantCourseAccessResponse(
            success=True
        )

    async def RevokeAccess(self, request, context):
        dto = RevokeCourseAccessDTO(
            user_id=request.user_id,
            course_id=request.course_id,
        )

        try:
            success = await self.service.revoke.execute(dto)
        except Exception as e:
            await context.abort(
                grpc.StatusCode.INTERNAL,
                str(e),
            )

        return pb2.RevokeCourseAccessResponse(
            success=success
        )

    async def HasAccess(self, request, context):
        dto = CheckCourseAccessDTO(
            user_id=request.user_id,
            course_id=request.course_id,
        )

        try:
            has_access = await self.service.has_access.execute(dto)
        except Exception as e:
            await context.abort(
                grpc.StatusCode.INTERNAL,
                str(e),
            )

        return pb2.HasCourseAccessResponse(
            has_access=has_access
        )
