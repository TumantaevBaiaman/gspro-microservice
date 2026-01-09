from src.infrastructure.db.mongo.repositories import *

from src.application.services import *


def build_services() -> dict[type, object]:
    return {
        ChatService: ChatService(
            repo=ChatRepository(),
        ),
        ChatMessageService: ChatMessageService(
            message_repo=ChatMessageRepository(),
        ),
        ChatParticipantService: ChatParticipantService(
            repo=ChatParticipantRepository(),
        )
    }

