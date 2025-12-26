from src.application.commands.favorite_course.dto import RemoveFromFavoritesDTO
from src.domain.repositories.favorite_course_repository import (
    IFavoriteCourseRepository,
)


class RemoveFromFavoritesCommand:
    def __init__(self, repo: IFavoriteCourseRepository):
        self.repo = repo

    async def execute(self, dto: RemoveFromFavoritesDTO) -> bool:
        return await self.repo.remove(
            user_id=dto.user_id,
            course_id=dto.course_id,
        )
