from abc import ABC, abstractmethod


class GoogleOAuthPort(ABC):

    @abstractmethod
    async def get_user_info(self, access_token: str) -> dict:
        pass
