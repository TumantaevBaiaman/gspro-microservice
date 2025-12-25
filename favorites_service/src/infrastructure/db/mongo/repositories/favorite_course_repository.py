from src.domain.repositories.favorite_course_repository import (
    IFavoriteCourseRepository,
)
from src.infrastructure.db.mongo.models.favorite_course import (
    FavoriteCourseDocument,
)


class FavoriteCourseRepository(IFavoriteCourseRepository):

    async def add(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> FavoriteCourseDocument:
        doc = FavoriteCourseDocument(
            user_id=user_id,
            course_id=course_id,
        )
        await doc.insert()
        return doc

    async def remove(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> bool:
        result = await FavoriteCourseDocument.find(
            FavoriteCourseDocument.user_id == user_id,
            FavoriteCourseDocument.course_id == course_id,
        ).delete()

        return result.deleted_count > 0

    async def list_by_user(
        self,
        *,
        user_id: str,
        limit: int,
        offset: int,
    ):
        query = FavoriteCourseDocument.find(
            FavoriteCourseDocument.user_id == user_id
        )

        total = await query.count()

        items = await (
            query
            .skip(offset)
            .limit(limit)
            .to_list()
        )

        return items, total

    async def is_favorite(
        self,
        *,
        user_id: str,
        course_id: str,
    ) -> bool:
        return await FavoriteCourseDocument.find(
            FavoriteCourseDocument.user_id == user_id,
            FavoriteCourseDocument.course_id == course_id,
        ).exists()
