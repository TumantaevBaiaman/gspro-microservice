import grpc
from fastapi import HTTPException
from google.protobuf.json_format import ParseDict, MessageToDict

from generated.course import category_pb2 as pb2
from generated.course import category_pb2_grpc as pb2_grpc


class CategoryClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("course_service:50052")
        self.stub = pb2_grpc.CourseCategoryServiceStub(self.channel)

    def get_category(self, category_id: str):
        try:
            res = self.stub.GetCategory(pb2.GetCategoryRequest(id=category_id))
            return MessageToDict(res)
        except grpc.RpcError as e:
            self._err(e)

    def list_categories(self, limit: int = 10, offset: int = 0):
        try:
            res = self.stub.ListCategories(
                pb2.ListCategoriesRequest(
                    limit=limit,
                    offset=offset
                )
            )
            return {
                "items": [MessageToDict(item) for item in res.items],
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


category_client = CategoryClient()