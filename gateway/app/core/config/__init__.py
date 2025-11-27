from .app_settings import AppSettings
from .service_settings import ServiceSettings
from .jwt_settings import JWTSettings

class Settings:
    app: AppSettings = AppSettings()
    services: ServiceSettings = ServiceSettings()
    jwt: JWTSettings = JWTSettings()


settings = Settings()