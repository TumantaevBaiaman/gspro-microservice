class ListAppFeedbackQuery:
    def __init__(self, repo):
        self.repo = repo

    async def execute(
        self,
        *,
        limit: int,
        offset: int,
    ):
        return await self.repo.list(
            limit=limit,
            offset=offset,
        )
