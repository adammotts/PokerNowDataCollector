# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "PokerNowData"
    API_V1_STR: str = "/api/v1"
    MONGODB_URL: str
    DATABASE_NAME: str = "pokernow_db"
    SECRET_KEY: str = "pokernow"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()
