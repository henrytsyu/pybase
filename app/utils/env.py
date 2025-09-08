from typing import Final

from pydantic_settings import BaseSettings, SettingsConfigDict


class Env(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", validate_assignment=True)

    SENTRY_DSN: str


ENV: Final[Env] = Env()  # type: ignore[call-arg]
