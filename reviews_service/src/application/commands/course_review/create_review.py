from src.application.commands.course_review.dto import CreateReviewDTO


class CreateReviewCommand:
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, dto: CreateReviewDTO):
        exists = await self.repo.exists_by_user_and_course(
            course_id=dto.course_id,
            user_id=dto.user_id,
        )
        if exists:
            raise ValueError("Review already exists")

        return await self.repo.create(
            course_id=dto.course_id,
            user_id=dto.user_id,
            rating=dto.rating,
            comment=dto.comment,
            tags=dto.tags,
        )