import grpc

from generated.course import category_pb2 as pb2
from generated.course import category_pb2_grpc as pb2_grpc
from src.application.services import CategoryService


class CategoryHandler(pb2_grpc.CourseCategoryServiceServicer):

    def __init__(self, service: CategoryService):
        self.service = service

    async def GetCategory(self, request, context):
        try:
            category = await self.service.get.execute(request.id)

            return pb2.GetCategoryResponse(
                id=str(category.id),
                title=category.title,
                codename=category.codename,
                parent_id=category.parent_id or "",
            )

        except Exception as e:
            await context.abort(
                grpc.StatusCode.NOT_FOUND,
                str(e)
            )

    async def ListCategories(self, request, context):
        result = await self.service.list.execute(
            limit=request.limit,
            offset=request.offset
        )

        response = pb2.ListCategoriesResponse(total=result.total)

        for category in result.items:
            response.items.append(
                pb2.CategoryItem(
                    id=str(category.id),
                    title=category.title,
                    codename=category.codename,
                    parent_id=category.parent_id or "",
                )
            )

        return response