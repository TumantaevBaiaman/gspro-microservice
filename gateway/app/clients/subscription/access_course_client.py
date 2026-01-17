import grpc
from fastapi import HTTPException

from generated.subscription import course_access_pb2 as pb2
from generated.subscription import course_access_pb2_grpc as pb2_grpc


class CourseAccessClient:
    def __init__(self):
        self.channel = grpc.insecure_channel(
            "subscription_service:50057"
        )
        self.stub = pb2_grpc.CourseAccessServiceStub(
            self.channel
        )

    def grant(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> bool:
        try:
            res = self.stub.GrantAccess(
                pb2.GrantCourseAccessRequest(
                    user_id=user_id,
                    course_id=course_id,
                ),
                timeout=3.0,
            )

            return res.success

        except grpc.RpcError as e:
            self._err(e)

    def revoke(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> bool:
        try:
            res = self.stub.RevokeAccess(
                pb2.RevokeCourseAccessRequest(
                    user_id=user_id,
                    course_id=course_id,
                ),
                timeout=3.0,
            )

            return res.success

        except grpc.RpcError as e:
            self._err(e)

    def has_access(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> bool:
        try:
            res = self.stub.HasAccess(
                pb2.HasCourseAccessRequest(
                    user_id=user_id,
                    course_id=course_id,
                ),
                timeout=3.0,
            )

            return res.has_access

        except grpc.RpcError as e:
            self._err(e)

    def list_user_courses(
            self,
            *,
            user_id: str,
    ) -> list[str]:
        try:
            res = self.stub.ListUserCourses(
                pb2.ListUserCoursesRequest(
                    user_id=user_id,
                ),
                timeout=3.0,
            )

            return list(res.course_ids)

        except grpc.RpcError as e:
            self._err(e)

    @staticmethod
    def _err(e: grpc.RpcError):
        code = e.code()
        msg = e.details()

        if code == grpc.StatusCode.NOT_FOUND:
            raise HTTPException(404, msg)

        if code == grpc.StatusCode.PERMISSION_DENIED:
            raise HTTPException(403, msg)

        raise HTTPException(400, msg)


course_access_client = CourseAccessClient()
