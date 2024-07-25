from pathlib import Path

from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    db_user: str
    db_password: str
    db_name: str
    db_host: str
    db_port: int

    class Config:
        env_file = f'{Path(__file__).resolve().parent}/dev.env'
        env_file_encoding = 'utf-8'


DB_SETTINGS = DBSettings()
