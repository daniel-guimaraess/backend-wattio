from pydantic import BaseSettings

class Settigs(BaseSettings):

    DATABASE_URL: str = ""

    class Config:
        env_file = ".env"