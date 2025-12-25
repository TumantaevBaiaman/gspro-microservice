import grpc

from generated.favorites import course_favorites_pb2 as pb2
from generated.favorites import course_favorites_pb2_grpc as pb2_grpc

from src.application.services import FavoriteCourseService
from src.application.commands.favorite_course.dto import (
    AddToFavoritesDTO,
    RemoveFromFavoritesDTO,
)
from src.application.queries.favorite_course.dto import (
    ListUserFavoritesDTO,
    IsFavoriteDTO,
)


class FavoriteCourseHandler(pb2_grpc.FavoriteCourseServiceServicer):

    def __init__(self, service: FavoriteCourseService):
        self.service = service

    async def AddToFavorites(self, request, context):
        dto = AddToFavoritesDTO(
            user_id=request.user_id,
            course_id=request.course_id,
        )

        try:
            favorite = await self.service.add.execute(dto)
        except Exception as e:
            await context.abort(
                grpc.StatusCode.INTERNAL,
                str(e),
            )

        if favorite is None:
            return pb2.AddToFavoritesResponse()

        return pb2.AddToFavoritesResponse(
            favorite=self._map_favorite(favorite)
        )

    async def RemoveFromFavorites(self, request, context):
        dto = RemoveFromFavoritesDTO(
            user_id=request.user_id,
            course_id=request.course_id,
        )

        try:
            success = await self.service.remove.execute(dto)
        except Exception as e:
            await context.abort(
                grpc.StatusCode.INTERNAL,
                str(e),
            )

        return pb2.RemoveFromFavoritesResponse(
            success=success
        )

    async def ListUserFavorites(self, request, context):
        dto = ListUserFavoritesDTO(
            user_id=request.user_id,
            limit=request.limit,
            offset=request.offset,
        )

        try:
            items, total = await self.service.list_by_user.execute(dto)
        except Exception as e:
            await context.abort(
                grpc.StatusCode.INTERNAL,
                str(e),
            )

        return pb2.ListUserFavoritesResponse(
            items=[self._map_favorite(item) for item in items],
            total=total,
        )

    async def IsFavorite(self, request, context):
        dto = IsFavoriteDTO(
            user_id=request.user_id,
            course_id=request.course_id,
        )

        try:
            is_favorite = await self.service.is_favorite.execute(dto)
        except Exception as e:
            await context.abort(
                grpc.StatusCode.INTERNAL,
                str(e),
            )

        return pb2.IsFavoriteResponse(
            is_favorite=is_favorite
        )

    @staticmethod
    def _map_favorite(doc):
        return pb2.FavoriteCourse(
            id=str(doc.id),
            user_id=doc.user_id,
            course_id=doc.course_id,
            created_at=int(doc.created_at.timestamp()),
        )
