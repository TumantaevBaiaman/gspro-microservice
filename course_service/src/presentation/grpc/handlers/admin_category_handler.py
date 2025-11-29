import grpc
from fastapi import HTTPException

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
        try:
            category = await self.service.create_category(dto=dto)
            return pb2.AdminCreateCategoryResponse(id=str(category.id))
        except HTTPException as e:
            if e.status_code == 409:
                await context.abort(grpc.StatusCode.ALREADY_EXISTS, e.detail)

    async def AdminUpdateCategory(self, request, context):
        dto = admin_category_dto.AdminCategoryUpdateDTO(**MessageToDict(request))
        try:
            category = await self.service.update_category(category_id=request.id, dto=dto)
            return pb2.AdminCategoryUpdateResponse(id=str(category.id))
        except HTTPException as e:
            if e.status_code == 404:
                return context.abort(grpc.StatusCode.NOT_FOUND, e.detail)
            if e.status_code == 409:
                return context.abort(grpc.StatusCode.ALREADY_EXISTS, e.detail)

    async def AdminGetCategory(self, request, context):
        try:
            category = await self.service.get_category(request.id)
            return pb2.AdminGetCategoryResponse(
                id=str(category.id),
                title=category.title,
                codename=category.codename,
                parentId=category.parent_id or ""
            )
        except HTTPException as e:
            if e.status_code == 404:
                await context.abort(grpc.StatusCode.NOT_FOUND, e.detail)