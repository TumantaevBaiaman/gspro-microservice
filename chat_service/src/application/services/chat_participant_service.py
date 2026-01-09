from src.application.commands.chat_participant.add import (
    AddChatParticipantCommand,
)
from src.application.commands.chat_participant.update import (
    UpdateLastReadCommand,
)
from src.application.commands.chat_participant.mute import (
    MuteChatParticipantCommand,
)
from src.application.commands.chat_participant.unmute import (
    UnmuteChatParticipantCommand,
)
from src.application.commands.chat_participant.archive import (
    ArchiveChatForUserCommand,
)
from src.application.commands.chat_participant.unarchive import (
    UnarchiveChatForUserCommand,
)

from src.application.queries.chat_participant.exist import (
    ExistsChatParticipantQuery,
)
from src.application.queries.chat_participant.list import (
    ListChatParticipantsQuery,
)
from src.application.queries.chat_participant.list_by_user import (
    ListChatIdsByUserQuery,
)

from src.domain.repositories.chat_participant_repository import (
    IChatParticipantRepository,
)


class ChatParticipantService:
    def __init__(self, repo: IChatParticipantRepository):
        self.add = AddChatParticipantCommand(repo)
        self.update_last_read = UpdateLastReadCommand(repo)
        self.mute = MuteChatParticipantCommand(repo)
        self.unmute = UnmuteChatParticipantCommand(repo)
        self.archive = ArchiveChatForUserCommand(repo)
        self.unarchive = UnarchiveChatForUserCommand(repo)

        self.exists = ExistsChatParticipantQuery(repo)
        self.list_by_chat = ListChatParticipantsQuery(repo)
        self.list_chat_ids_by_user = ListChatIdsByUserQuery(repo)
