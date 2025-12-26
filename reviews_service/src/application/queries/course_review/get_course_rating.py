class GetCourseRatingQuery:
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, *, course_id: str):
        return await self.repo.get_course_rating(course_id=course_id)