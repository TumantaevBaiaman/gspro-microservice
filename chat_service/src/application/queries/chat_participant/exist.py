from src.application.queries.chat_participant.dto import CheckChatParticipantDTO
from src.domain.repositories import IChatParticipantRepository


class ExistsChatParticipantQuery:

    def __init__(self, repo: IChatParticipantRepository):
        self.repo = repo

    async def execute(self, dto: CheckChatParticipantDTO) -> bool:
        return await self.repo.exists(
            chat_id=dto.chat_id,
            user_id=dto.user_id,
        )
