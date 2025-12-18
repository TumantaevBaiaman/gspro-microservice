import grpc.aio
from fastapi import HTTPException

from generated.user import user_category_pb2_grpc, user_category_pb2
from google.protobuf.json_format import MessageToDict


class UserCategoryClient:
    def __init__(self):
        self.channel = grpc.aio.insecure_channel("user_service:50051")
        self.stub = user_category_pb2_grpc.UserCategoryServiceStub(self.channel)

    async def list_user_categories(self, user_id: str, limit: int = 10, offset: int = 0):
        request = user_category_pb2.ListUserCategoriesRequest(user_id=user_id, limit=limit, offset=offset)
        try:
            response = await self.stub.ListUserCategories(request)
            return response
        except grpc.RpcError as e:
            print(e)
            raise HTTPException(status_code=500, detail="Internal error")

    async def create_user_category(self, user_id, data):
        request = user_category_pb2.AddUserCategoryRequest(
            user_id=user_id,
            categories=data.categories,
        )
        try:
            response = await self.stub.AddUserCategory(request)
            return response
        except grpc.RpcError as e:
            print(e)
            if e.code() == grpc.StatusCode.ALREADY_EXISTS:
                raise HTTPException(status_code=409, detail=e.details())
            raise HTTPException(status_code=500, detail="Internal error")

    async def delete_user_category(self, user_id, id):
        request = user_category_pb2.RemoveUserCategoryRequest(
            user_id=user_id,
            id=id,
        )
        try:
            response = await self.stub.RemoveUserCategory(request)
            return response
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise HTTPException(status_code=404, detail=e.details())
            raise HTTPException(status_code=500, detail="Internal error")


user_category_client = UserCategoryClient()