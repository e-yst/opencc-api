from pydantic_settings import BaseSettings

from app.core.constants import Environment


class Config(BaseSettings):
    PROJECT_NAME: str = "OpenCC API"

    ENVIRONMENT: Environment = Environment.DEVELOPMENT

    CORS_ORIGINS: list[str] = ["*"]
    CORS_ORIGINS_REGEX: str | None = None

    @property
    def is_debug(self):
        return self.ENVIRONMENT.is_debug


settings = Config()
