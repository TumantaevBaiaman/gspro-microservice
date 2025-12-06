import grpc
from fastapi import HTTPException
from google.protobuf.json_format import ParseDict, MessageToDict

from generated.course import admin_course_pb2 as pb2
from generated.course import admin_course_pb2_grpc as pb2_grpc


class AdminCourseClient:
    def __init__(self, host="course_service", port=50052):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = pb2_grpc.AdminCourseServiceStub(self.channel)

    def create_course(self, dto):
        req = ParseDict(dto.model_dump(), pb2.AdminCreateCourseRequest())
        try:
            return self.stub.AdminCreateCourse(req)
        except grpc.RpcError as e:
            self._err(e)

    def get_course(self, course_id: str):
        try:
            res = self.stub.AdminGetCourse(pb2.AdminGetCourseRequest(id=course_id))
            return MessageToDict(res)
        except grpc.RpcError as e:
            self._err(e)

    # UPDATE
    def update_course(self, course_id, dto):
        req = pb2.AdminUpdateCourseRequest(id=course_id, **dto.model_dump(exclude_unset=True))
        try:
            return self.stub.AdminUpdateCourse(req)
        except grpc.RpcError as e:
            self._err(e)

    def delete_course(self, course_id):
        try:
            return self.stub.AdminDeleteCourse(pb2.AdminDeleteCourseRequest(id=course_id))
        except grpc.RpcError as e:
            self._err(e)

    def list_courses(self, category_id=None):
        req = pb2.AdminListCoursesRequest(category_id=category_id or "")
        try:
            res = self.stub.AdminListCourses(req)
            return MessageToDict(res)
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


admin_course_client = AdminCourseClient()
