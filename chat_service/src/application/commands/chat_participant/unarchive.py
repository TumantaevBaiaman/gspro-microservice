from src.application.commands.chat_participant.dto import UnarchiveChatForUserDTO
from src.domain.repositories import IChatParticipantRepository


class UnarchiveChatForUserCommand:

    def __init__(self, repo: IChatParticipantRepository):
        self.repo = repo

    async def execute(self, dto: UnarchiveChatForUserDTO) -> None:
        await self.repo.set_archived(
            chat_id=dto.chat_id,
            user_id=dto.user_id,
            value=False,
        )
