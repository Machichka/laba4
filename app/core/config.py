from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    # Змінні для бази даних з дефолтними значеннями (якщо .env не зчитався)
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "fastapi_db"

    # Налаштування JWT (Захист Лаби 5)
    SECRET_KEY: str = "SUPER_SECRET_KEY_KUDY_ZH_BEZ_NYOGO"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Автоматично збираємо DATABASE_URL
    @property
    def DATABASE_URL(self) -> str:
        # Для асинхронної роботи використовуємо префікс postgresql+asyncpg
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # Налаштування для Pydantic v2 (правильне зчитування .env на будь-якій ОС)
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()