import grpc
from fastapi import HTTPException
from google.protobuf.json_format import ParseDict, MessageToDict

from generated.course import admin_category_pb2 as pb2
from generated.course import admin_category_pb2_grpc as pb2_grpc


class AdminCategoryClient:
    def __init__(self, host="course_service", port=50052):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = pb2_grpc.AdminCategoryServiceStub(self.channel)

    def create_category(self, dto):
        request = ParseDict(dto.model_dump(), pb2.AdminCreateCategoryRequest())

        try:
            return self.stub.AdminCreateCategory(request)
        except grpc.RpcError as e:
            self._handle_error(e)

    def get_category(self, category_id: str):
        request = pb2.AdminGetCategoryRequest(id=category_id)

        try:
            return self.stub.AdminGetCategory(request)
        except grpc.RpcError as e:
            self._handle_error(e)

    def update_category(self, category_id: str, dto):
        request = pb2.AdminUpdateCategoryRequest(id=category_id, **dto.model_dump(exclude_unset=True))

        try:
            return self.stub.AdminUpdateCategory(request)
        except grpc.RpcError as e:
            self._handle_error(e)

    def delete_category(self, category_id: str):
        request = pb2.AdminDeleteCategoryRequest(id=category_id)

        try:
            return self.stub.AdminDeleteCategory(request)
        except grpc.RpcError as e:
            print(e)
            self._handle_error(e)

    @staticmethod
    def _handle_error(e: grpc.RpcError):
        code = e.code()
        msg = e.details()

        match code:
            case grpc.StatusCode.NOT_FOUND:
                raise HTTPException(status_code=404, detail=msg)
            case grpc.StatusCode.ALREADY_EXISTS:
                raise HTTPException(status_code=409, detail=msg)
            case _:
                raise HTTPException(status_code=400, detail=msg)


admin_category_client = AdminCategoryClient()
