import os

DEBUG = bool(os.getenv('DEBUG', False))


class DBSettings:
    db_user: str = os.getenv('DB_USER')
    db_password: str = os.getenv('DB_PASSWORD')
    db_name: str = os.getenv('DB_NAME')
    db_host: str = os.getenv('DB_HOST')
    db_port: int = int(os.getenv('DB_PORT'))


DB_SETTINGS = DBSettings()
