import grpc
from fastapi import HTTPException
from google.protobuf.json_format import MessageToDict

from generated.course import course_pb2 as pb2
from generated.course import course_pb2_grpc as pb2_grpc


class CourseClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("course_service:50052")
        self.stub = pb2_grpc.CourseServiceStub(self.channel)

    def get_course(self, course_id: str) -> dict:
        try:
            res = self.stub.GetCourse(
                pb2.GetCourseRequest(id=course_id),
                timeout=3.0
            )
            return MessageToDict(
                res,
                preserving_proto_field_name=True
            )
        except grpc.RpcError as e:
            self._err(e)

    def list_courses(self, limit: int = 10, offset: int = 0, mode: str = "all", author_id: str | None = None,) -> dict:
        try:
            res = self.stub.ListCourses(
                pb2.ListCoursesRequest(
                    limit=limit,
                    offset=offset,
                    mode=mode,
                    author_id=author_id
                ),
                timeout=3.0
            )
            return {
                "items": [
                    MessageToDict(
                        item,
                        preserving_proto_field_name=True
                    )
                    for item in res.items
                ],
                "total": res.total
            }
        except grpc.RpcError as e:
            self._err(e)

    @staticmethod
    def _err(e: grpc.RpcError):
        code = e.code()
        msg = e.details()

        if code == grpc.StatusCode.NOT_FOUND:
            raise HTTPException(404, msg)
        if code == grpc.StatusCode.ALREADY_EXISTS:
            raise HTTPException(409, msg)

        raise HTTPException(400, msg)


course_client = CourseClient()

