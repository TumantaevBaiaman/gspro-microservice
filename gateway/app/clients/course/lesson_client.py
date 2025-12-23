import grpc
from fastapi import HTTPException
from google.protobuf.json_format import MessageToDict

from generated.course import lesson_pb2 as pb2
from generated.course import lesson_pb2_grpc as pb2_grpc


class LessonClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("course_service:50052")
        self.stub = pb2_grpc.LessonServiceStub(self.channel)

    def get_lesson(self, lesson_id: str) -> dict:
        try:
            res = self.stub.GetLesson(
                pb2.GetLessonRequest(id=lesson_id),
                timeout=3.0
            )

            return MessageToDict(
                res.lesson,
                preserving_proto_field_name=True
            )

        except grpc.RpcError as e:
            self._err(e)

    def list_lessons_by_module(self, module_id: str) -> list[dict]:
        try:
            res = self.stub.ListLessonsByModule(
                pb2.ListLessonsByModuleRequest(module_id=module_id),
                timeout=3.0
            )

            return [
                MessageToDict(
                    item,
                    preserving_proto_field_name=True
                )
                for item in res.items
            ]

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


lesson_client = LessonClient()
