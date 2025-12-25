from src.application.queries.favorite_course.dto import ListUserFavoritesDTO
from src.domain.repositories.favorite_course_repository import (
    IFavoriteCourseRepository,
)


class ListUserFavoritesQuery:
    def __init__(self, repo: IFavoriteCourseRepository):
        self.repo = repo

    async def execute(self, dto: ListUserFavoritesDTO):
        return await self.repo.list_by_user(
            user_id=dto.user_id,
            limit=dto.limit,
            offset=dto.offset,
        )
