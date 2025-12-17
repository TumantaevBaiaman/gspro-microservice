import httpx
from src.application.ports.google_oauth_port import GoogleOAuthPort


class GoogleOAuthClient(GoogleOAuthPort):

    async def get_user_info(self, access_token: str) -> dict:
        async with httpx.AsyncClient(timeout=5) as client:
            resp = await client.get(
                "https://www.googleapis.com/oauth2/v3/userinfo",
                headers={"Authorization": f"Bearer {access_token}"}
            )

        if resp.status_code != 200:
            raise ValueError("Invalid Google token")

        return resp.json()