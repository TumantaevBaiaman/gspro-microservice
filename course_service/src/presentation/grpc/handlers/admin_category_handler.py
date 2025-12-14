import grpc

from generated.course import admin_category_pb2 as pb2
from generated.course import admin_category_pb2_grpc as pb2_grpc

from google.protobuf.json_format import MessageToDict

from src.domain.dto import admin_category_dto
from src.application.services.admin_category_service import AdminCategoryService
from src.domain.exceptions.admin_category import (
    CategoryAlreadyExistsError,
    CategoryNotFoundError,
)


class AdminCategoryHandler(pb2_grpc.AdminCategoryServiceServicer):

    def __init__(self, service: AdminCategoryService):
        self.service = service

    async def AdminCreateCategory(self, request, context):
        dto = admin_category_dto.AdminCategoryCreateDTO(
            **MessageToDict(request, preserving_proto_field_name=True)
        )
        try:
            category = await self.service.create.execute(dto)
            return pb2.AdminCreateCategoryResponse(id=str(category.id))

        except CategoryAlreadyExistsError as e:
            await context.abort(
                grpc.StatusCode.ALREADY_EXISTS,
                str(e),
            )

    async def AdminUpdateCategory(self, request, context):
        dto = admin_category_dto.AdminCategoryUpdateDTO(
            **MessageToDict(request, preserving_proto_field_name=True)
        )
        try:
            category = await self.service.update.execute(request.id, dto)
            return pb2.AdminUpdateCategoryResponse(
                id=str(category.id),
                title=category.title,
                codename=category.codename,
                parent_id=category.parent_id or "",
            )

        except CategoryNotFoundError as e:
            await context.abort(
                grpc.StatusCode.NOT_FOUND,
                str(e),
            )
        except CategoryAlreadyExistsError as e:
            await context.abort(
                grpc.StatusCode.ALREADY_EXISTS,
                str(e),
            )

    async def AdminGetCategory(self, request, context):
        try:
            category = await self.service.get.execute(request.id)
            return pb2.AdminGetCategoryResponse(
                id=str(category.id),
                title=category.title,
                codename=category.codename,
                parent_id=category.parent_id or "",
            )

        except CategoryNotFoundError as e:
            await context.abort(
                grpc.StatusCode.NOT_FOUND,
                str(e),
            )

    async def AdminDeleteCategory(self, request, context):
        try:
            await self.service.delete.execute(request.id)
            return pb2.AdminDeleteCategoryResponse(success=True)

        except CategoryNotFoundError as e:
            await context.abort(
                grpc.StatusCode.NOT_FOUND,
                str(e),
            )