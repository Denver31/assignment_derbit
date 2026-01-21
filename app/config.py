from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    TEST_DB_NAME: str
    REDIS_URL: str

    model_config = ConfigDict(
        env_file=".env",
    )

settings = Settings()
