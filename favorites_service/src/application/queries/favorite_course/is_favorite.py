from src.application.queries.favorite_course.dto import IsFavoriteDTO
from src.domain.repositories.favorite_course_repository import (
    IFavoriteCourseRepository,
)


class IsFavoriteQuery:
    def __init__(self, repo: IFavoriteCourseRepository):
        self.repo = repo

    async def execute(self, dto: IsFavoriteDTO) -> bool:
        return await self.repo.is_favorite(
            user_id=dto.user_id,
            course_id=dto.course_id,
        )
