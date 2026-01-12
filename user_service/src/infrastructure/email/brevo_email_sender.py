import os
import requests

from src.core.config import settings


class BrevoEmailSender:
    def __init__(self):
        self.api_key = settings.BREVO_API_KEY
        self.email = settings.BREVO_EMAIL
        self.base_url = "https://api.brevo.com/v3/smtp/email"

    async def send_password_reset_code(self, to: str, code: str):
        payload = {
            "sender": {
                "email": f"{self.email}",
                "name": "GS PRO"
            },
            "to": [
                {"email": to}
            ],
            "subject": "Код для сброса пароля",
            "htmlContent": f"""
                <h2>Сброс пароля</h2>
                <p>Ваш код:</p>
                <h1>{code}</h1>
                <p>Код действует 10 минут.</p>
                <p>Если вы не запрашивали сброс — просто игнорируйте это письмо.</p>
            """
        }

        response = requests.post(
            self.base_url,
            headers={
                "api-key": self.api_key,
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=10,
        )
        if response.status_code >= 400:
            raise RuntimeError(
                f"Brevo error {response.status_code}: {response.text}"
            )
