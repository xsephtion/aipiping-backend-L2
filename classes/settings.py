import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str = os.environ.get('OPEN_AI_KEY')

    class Config:
        env_file = '.env'