from src.application.commands.chat_message.send import (
    SendMessageCommand,
)
from src.application.commands.chat_message.edit import (
    EditMessageCommand,
)
from src.application.commands.chat_message.delete import (
    DeleteMessageCommand,
)

from src.application.queries.chat_message.get_by_id import (
    GetMessageByIdQuery,
)
from src.application.queries.chat_message.list_by_chat import (
    ListMessagesByChatQuery,
)
from src.application.queries.chat_message.list_by_reference import (
    ListMessagesByReferenceQuery,
)

from src.domain.repositories.chat_message_repository import (
    IChatMessageRepository,
)
from src.domain.repositories.chat_participant_repository import (
    IChatParticipantRepository,
)


class ChatMessageService:
    def __init__(
        self,
        message_repo: IChatMessageRepository,
        participant_repo: IChatParticipantRepository,
    ):
        self.send = SendMessageCommand(
            message_repo=message_repo,
            participant_repo=participant_repo,
        )
        self.edit = EditMessageCommand(message_repo)
        self.delete = DeleteMessageCommand(message_repo)

        self.get = GetMessageByIdQuery(message_repo)
        self.list_by_chat = ListMessagesByChatQuery(message_repo)
        self.list_by_reference = ListMessagesByReferenceQuery(message_repo)
