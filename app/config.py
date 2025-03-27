from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    shared_url: str
    database_url_1: str
    database_url_2: str
    database_url_3: str
    database_url_4: str

    class Config:
        env_file= ".env"

settings = Settings()
