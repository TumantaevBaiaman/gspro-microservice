import grpc
from google.protobuf.json_format import MessageToDict

from generated.course import admin_module_pb2 as pb2
from generated.course import admin_module_pb2_grpc as pb2_grpc

from src.domain.dto.admin_module_dto import (
    AdminModuleCreateDTO,
    AdminModuleUpdateDTO,
)
from src.domain.exceptions.admin_module import ModuleNotFoundError
from src.application.services.admin_module_service import AdminModuleService


class AdminModuleHandler(pb2_grpc.AdminModuleServiceServicer):

    def __init__(self, service: AdminModuleService):
        self.service = service

    async def AdminCreateModule(self, request, context):
        dto = AdminModuleCreateDTO(**MessageToDict(request))

        module = await self.service.create.execute(dto)

        return pb2.AdminCreateModuleResponse(
            id=str(module.id)
        )

    async def AdminGetModule(self, request, context):
        try:
            module = await self.service.get.execute(request.id)

            return pb2.AdminGetModuleResponse(
                id=str(module.id),
                course_id=module.course_id,
                title=module.title,
                description=module.description or "",
                order_number=module.order_number or 0,
            )

        except ModuleNotFoundError as e:
            await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

    async def AdminUpdateModule(self, request, context):
        dto = AdminModuleUpdateDTO(**MessageToDict(request))

        try:
            module = await self.service.update.execute(
                module_id=request.id,
                dto=dto,
            )

            return pb2.AdminUpdateModuleResponse(
                id=str(module.id)
            )

        except ModuleNotFoundError as e:
            await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

    async def AdminDeleteModule(self, request, context):
        try:
            await self.service.delete.execute(request.id)

            return pb2.AdminDeleteModuleResponse(
                success=True
            )

        except ModuleNotFoundError as e:
            await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

    async def AdminListModules(self, request, context):
        modules = await self.service.list.execute(
            course_id=request.course_id or None
        )

        response = pb2.AdminListModulesResponse()

        for module in modules:
            response.items.add(
                id=str(module.id),
                course_id=module.course_id,
                title=module.title,
                description=module.description or "",
                order_number=module.order_number or 0,
            )

        return response
