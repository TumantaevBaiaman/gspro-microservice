from .app_settings import AppSettings
from .service_settings import ServiceSettings
from .jwt_settings import JWTSettings
from .media_settings import MediaSettings


class Settings:
    app: AppSettings = AppSettings()
    services: ServiceSettings = ServiceSettings()
    jwt: JWTSettings = JWTSettings()
    media: MediaSettings = MediaSettings()


settings = Settings()