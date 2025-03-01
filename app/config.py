import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BASE_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str
    
    @property
    def DB_URL(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:" \
               f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:" \
               f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    SECRET_KEY: str
    ALGORITHM: str

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env")

settings = Settings()
database_url = settings.DB_URL