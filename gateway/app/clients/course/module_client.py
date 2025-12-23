import grpc
from fastapi import HTTPException
from google.protobuf.json_format import MessageToDict

from generated.course import module_pb2 as pb2
from generated.course import module_pb2_grpc as pb2_grpc


class ModuleClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("course_service:50052")
        self.stub = pb2_grpc.ModuleServiceStub(self.channel)

    def get_module(self, module_id: str) -> dict:
        try:
            res = self.stub.GetModule(
                pb2.GetModuleRequest(id=module_id),
                timeout=3.0
            )
            return MessageToDict(
                res,
                preserving_proto_field_name=True
            )
        except grpc.RpcError as e:
            self._err(e)

    def list_modules_by_course(self, course_id: str) -> list[dict]:
        try:
            res = self.stub.ListModulesByCourse(
                pb2.ListModulesByCourseRequest(course_id=course_id),
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


module_client = ModuleClient()
