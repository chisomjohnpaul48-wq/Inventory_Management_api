from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent
class Settings(BaseSettings):
    DATABASE_URL: str
    TEST_DATABASE_URL: str
    APP_NAME: str = "Inventory Management API"
    DEBUG: bool = False

    model_config = SettingsConfigDict(env_file=BASE_DIR/".env", extra="ignore")

settings = Settings()   #type: ignore

