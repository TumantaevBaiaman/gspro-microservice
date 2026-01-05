import grpc

from generated.course import module_pb2 as pb2
from generated.course import module_pb2_grpc as pb2_grpc

from src.application.services.module_service import ModuleService
from src.domain.exceptions.module import ModuleNotFoundError


class ModuleHandler(pb2_grpc.ModuleServiceServicer):

    def __init__(self, service: ModuleService):
        self.service = service

    async def GetModule(self, request, context):
        try:
            module = await self.service.get(request.id)

            return pb2.GetModuleResponse(
                id=str(module.id),
                course_id=module.course_id,
                title=module.title,
                description=module.description or "",
                order_number=module.order_number or 0,
            )

        except ModuleNotFoundError as e:
            await context.abort(grpc.StatusCode.NOT_FOUND, str(e))

    async def ListModulesByCourse(self, request, context):
        modules = await self.service.list_by_course(request.course_id)

        return pb2.ListModulesResponse(
            items=[
                pb2.Module(
                    id=str(module.id),
                    course_id=module.course_id,
                    title=module.title,
                    description=module.description or "",
                    order_number=module.order_number or 0,
                    lessons_count=await self.service.get_lessons_count.execute(module.id)
                )
                for module in modules
            ]
        )
