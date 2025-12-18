import grpc

import generated.user.user_category_pb2 as pb2
import generated.user.user_category_pb2_grpc as pb2_grpc

from src.infrastructure.db.session import async_session_maker
from src.presentation.grpc.container import Container
from src.domain.exceptions.user_category import UserCategoryNotFoundError


class UserCategoryHandler(pb2_grpc.UserCategoryServiceServicer):
    async def ListUserCategories(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            categories, total = await container.user_category_service.list_user_categories.execute(
                user_id=request.user_id,
                limit=request.limit,
                offset=request.offset
            )
            return pb2.ListUserCategoriesResponse(
                items=[
                    pb2.UserCategoryItem(
                        id=str(category.id),
                        category_id=str(category.category_id),
                        user_id=str(category.user_id)
                    )
                    for category in categories
                ],
                total=total
            )

    async def AddUserCategory(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            try:
                await container.user_category_service.create_user_category.execute(
                    user_id=request.user_id,
                    categories=request.categories
                )
                await container.uow.commit()
            except UserCategoryNotFoundError as e:
                await container.uow.rollback()
                await context.abort(
                    grpc.StatusCode.NOT_FOUND,
                    str(e)
                )

            return pb2.AddUserCategoryResponse(
                success=True
            )

    async def RemoveUserCategory(self, request, context):
        async with async_session_maker() as session:
            container = Container(session)

            try:
                await container.user_category_service.delete_user_category.execute(
                    user_id=request.user_id,
                    id=request.id
                )
                await container.uow.commit()
            except UserCategoryNotFoundError as e:
                await container.uow.rollback()
                await context.abort(
                    grpc.StatusCode.NOT_FOUND,
                    str(e)
                )

            return pb2.RemoveUserCategoryResponse()


