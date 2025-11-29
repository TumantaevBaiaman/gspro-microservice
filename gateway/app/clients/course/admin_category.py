import grpc
from fastapi import HTTPException

from google.protobuf.json_format import ParseDict

from generated.course import admin_category_pb2, admin_category_pb2_grpc


class AdminCategoryClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("course_service:50052")
        self.stub = admin_category_pb2_grpc.AdminCategoryServiceStub(self.channel)

    def create_category(self, data):
        request = ParseDict(data.dict(), admin_category_pb2.AdminCreateCategoryRequest())

        try:
            response = self.stub.AdminCreateCategory(request)
            return response
        except grpc.RpcError as e:
            status = e.code()
            message = e.details()

            if status == grpc.StatusCode.ALREADY_EXISTS:
                raise HTTPException(status_code=409, detail=message)

            raise HTTPException(status_code=400, detail=message)


admin_category_client = AdminCategoryClient()