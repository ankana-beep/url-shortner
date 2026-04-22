
from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://localhost:27017"
    REDIS_URI: str = "redis://127.0.0.1:6379"
    BASE_URL: str = "http://127.0.0.1:8081"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
