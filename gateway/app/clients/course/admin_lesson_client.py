import grpc
from fastapi import HTTPException
from google.protobuf.json_format import ParseDict, MessageToDict

from generated.course import admin_lesson_pb2 as pb2
from generated.course import admin_lesson_pb2_grpc as pb2_grpc


class AdminLessonClient:
    def __init__(self, host="course_service", port=50052):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = pb2_grpc.AdminLessonServiceStub(self.channel)

    def create_lesson(self, dto):
        req = ParseDict(
            dto.model_dump(),
            pb2.AdminCreateLessonRequest(),
            ignore_unknown_fields=True,
        )
        try:
            return self.stub.AdminCreateLesson(req)
        except grpc.RpcError as e:
            self._err(e)

    def get_lesson(self, lesson_id):
        try:
            res = self.stub.AdminGetLesson(
                pb2.AdminGetLessonRequest(id=lesson_id)
            )
            return MessageToDict(
                res,
                preserving_proto_field_name=True,
            )
        except grpc.RpcError as e:
            self._err(e)

    def update_lesson(self, lesson_id, dto):
        req = pb2.AdminUpdateLessonRequest(
            id=lesson_id,
            **dto.model_dump(exclude_unset=True)
        )
        try:
            return self.stub.AdminUpdateLesson(req)
        except grpc.RpcError as e:
            self._err(e)

    def delete_lesson(self, lesson_id):
        try:
            return self.stub.AdminDeleteLesson(pb2.AdminDeleteLessonRequest(id=lesson_id))
        except grpc.RpcError as e:
            self._err(e)

    def list_lessons(self, module_id=None):
        req = pb2.AdminListLessonsRequest(module_id=module_id or "")
        try:
            res = self.stub.AdminListLessons(req)
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


admin_lesson_client = AdminLessonClient()
