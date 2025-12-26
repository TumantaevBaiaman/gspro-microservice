from src.application.commands.favorite_course.dto import AddToFavoritesDTO
from src.domain.repositories.favorite_course_repository import (
    IFavoriteCourseRepository,
)


class AddToFavoritesCommand:
    def __init__(self, repo: IFavoriteCourseRepository):
        self.repo = repo

    async def execute(self, dto: AddToFavoritesDTO):
        exists = await self.repo.is_favorite(
            user_id=dto.user_id,
            course_id=dto.course_id,
        )

        if exists:
            return None

        return await self.repo.add(
            user_id=dto.user_id,
            course_id=dto.course_id,
        )
