class ListUserCoursesQuery:
    def __init__(self, repository):
        self.repository = repository

    async def execute(self, dto):
        return await self.repository.list_user_courses(
            user_id=dto.user_id
        )
