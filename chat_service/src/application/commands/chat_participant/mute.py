from src.application.commands.chat_participant.dto import MuteChatParticipantDTO
from src.domain.repositories import IChatParticipantRepository


class MuteChatParticipantCommand:

    def __init__(self, repo: IChatParticipantRepository):
        self.repo = repo

    async def execute(self, dto: MuteChatParticipantDTO) -> None:
        await self.repo.set_muted(
            chat_id=dto.chat_id,
            user_id=dto.user_id,
            value=True,
        )
