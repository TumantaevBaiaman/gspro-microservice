import grpc
from fastapi import HTTPException
from google.protobuf.json_format import MessageToDict

from generated.course import admin_module_pb2 as pb2
from generated.course import admin_module_pb2_grpc as pb2_grpc

from src.domain.dto.admin_module_dto import AdminModuleCreateDTO, AdminModuleUpdateDTO
from src.application.services.admin_module_service import AdminModuleService


class AdminModuleHandler(pb2_grpc.AdminModuleServiceServicer):

    def __init__(self):
        self.service = AdminModuleService()

    async def AdminCreateModule(self, request, context):
        dto = AdminModuleCreateDTO(**MessageToDict(request))
        module = await self.service.create_module(dto)
        return pb2.AdminCreateModuleResponse(id=str(module.id))

    async def AdminGetModule(self, request, context):
        try:
            module = await self.service.get_module(request.id)
            return pb2.AdminGetModuleResponse(
                id=str(module.id),
                course_id=module.course_id,
                title=module.title,
                description=module.description or "",
                order_number=module.order_number or 0,
            )
        except HTTPException as e:
            if e.status_code == 404:
                await context.abort(grpc.StatusCode.NOT_FOUND, e.detail)

    async def AdminUpdateModule(self, request, context):
        dto = AdminModuleUpdateDTO(**MessageToDict(request))
        try:
            module = await self.service.update_module(request.id, dto)
            return pb2.AdminUpdateModuleResponse(id=str(module.id))
        except HTTPException as e:
            if e.status_code == 404:
                await context.abort(grpc.StatusCode.NOT_FOUND, e.detail)

    async def AdminDeleteModule(self, request, context):
        try:
            await self.service.delete_module(request.id)
            return pb2.AdminDeleteModuleResponse(success=True)
        except HTTPException as e:
            if e.status_code == 404:
                await context.abort(grpc.StatusCode.NOT_FOUND, e.detail)

    async def AdminListModules(self, request, context):
        modules = await self.service.list_modules(request.course_id or None)

        response = pb2.AdminListModulesResponse()
        for m in modules:
            response.items.add(
                id=str(m.id),
                course_id=m.course_id,
                title=m.title,
                description=m.description or "",
                order_number=m.order_number or 0
            )
        return response
