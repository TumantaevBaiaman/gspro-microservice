import grpc
from fastapi import HTTPException
from google.protobuf.json_format import ParseDict, MessageToDict

from generated.course import admin_module_pb2 as pb2
from generated.course import admin_module_pb2_grpc as pb2_grpc


class AdminModuleClient:
    def __init__(self, host="course_service", port=50052):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = pb2_grpc.AdminModuleServiceStub(self.channel)

    def create_module(self, dto):
        req = ParseDict(
            dto.model_dump(),
            pb2.AdminCreateModuleRequest(),
            ignore_unknown_fields=True
        )
        try:
            return self.stub.AdminCreateModule(req)
        except grpc.RpcError as e:
            self._err(e)

    def get_module(self, module_id):
        try:
            res = self.stub.AdminGetModule(
                pb2.AdminGetModuleRequest(id=module_id)
            )
            return MessageToDict(
                res,
                preserving_proto_field_name=True,
            )
        except grpc.RpcError as e:
            self._err(e)

    def update_module(self, module_id, dto):
        req = pb2.AdminUpdateModuleRequest(id=module_id, **dto.model_dump(exclude_unset=True))
        try:
            return self.stub.AdminUpdateModule(req)
        except grpc.RpcError as e:
            self._err(e)

    def delete_module(self, module_id):
        try:
            return self.stub.AdminDeleteModule(pb2.AdminDeleteModuleRequest(id=module_id))
        except grpc.RpcError as e:
            self._err(e)

    def list_modules(self, course_id=None):
        req = pb2.AdminListModulesRequest(course_id=course_id or "")
        try:
            res = self.stub.AdminListModules(req)
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


admin_module_client = AdminModuleClient()
