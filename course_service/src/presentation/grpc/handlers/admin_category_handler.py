import grpc

from generated.course import admin_category_pb2 as pb2
from generated.course import admin_category_pb2_grpc as pb2_grpc

from google.protobuf.json_format import MessageToDict

from src.domain.dto import admin_category_dto
from src.application.services.admin_category_service import AdminCategoryService


class AdminCategoryHandler(pb2_grpc.AdminCategoryServiceServicer):

    def __init__(self):
        self.service = AdminCategoryService()

    async def AdminCreateCategory(self, request, context):

        dto = admin_category_dto.AdminCategoryCreateDTO(**MessageToDict(request))

        category = await self.service.admin_create_category(dto)

        return pb2.AdminCreateCategoryResponse(id=str(category.id))

