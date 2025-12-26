import grpc
from fastapi import HTTPException
from google.protobuf.json_format import MessageToDict

from generated.favorites import course_favorites_pb2 as pb2
from generated.favorites import course_favorites_pb2_grpc as pb2_grpc


class FavoriteClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("favorites_service:50054")
        self.stub = pb2_grpc.FavoriteCourseServiceStub(self.channel)

    def add_to_favorites(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> dict:
        try:
            res = self.stub.AddToFavorites(
                pb2.AddToFavoritesRequest(
                    user_id=user_id,
                    course_id=course_id,
                ),
                timeout=3.0,
            )

            if not res.favorite.id:
                return {}

            return MessageToDict(
                res.favorite,
                preserving_proto_field_name=True,
            )

        except grpc.RpcError as e:
            self._err(e)

    def remove_from_favorites(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> bool:
        try:
            res = self.stub.RemoveFromFavorites(
                pb2.RemoveFromFavoritesRequest(
                    user_id=user_id,
                    course_id=course_id,
                ),
                timeout=3.0,
            )

            return res.success

        except grpc.RpcError as e:
            self._err(e)

    def list_user_favorites(
        self,
        *,
        user_id: str,
        limit: int,
        offset: int,
    ) -> dict:
        try:
            res = self.stub.ListUserFavorites(
                pb2.ListUserFavoritesRequest(
                    user_id=user_id,
                    limit=limit,
                    offset=offset,
                ),
                timeout=3.0,
            )

            return {
                "items": [
                    MessageToDict(
                        item,
                        preserving_proto_field_name=True,
                    )
                    for item in res.items
                ],
                "total": res.total,
            }

        except grpc.RpcError as e:
            self._err(e)

    def is_favorite(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> bool:
        try:
            res = self.stub.IsFavorite(
                pb2.IsFavoriteRequest(
                    user_id=user_id,
                    course_id=course_id,
                ),
                timeout=3.0,
            )

            return res.is_favorite

        except grpc.RpcError as e:
            self._err(e)

    @staticmethod
    def _err(e: grpc.RpcError):
        code = e.code()
        msg = e.details()

        if code == grpc.StatusCode.NOT_FOUND:
            raise HTTPException(404, msg)

        if code == grpc.StatusCode.ALREADY_EXISTS:
            raise HTTPException(409, msg)

        raise HTTPException(400, msg)


course_favorite_client = FavoriteClient()
