from peewee_async import AsyncDatabase
from peewee_asyncext import PostgresqlExtDatabase

from config import DB_SETTINGS, DBSettings


def create_database_from_settings(settings: DBSettings, db_creator) -> AsyncDatabase:
    _ = settings
    return db_creator(
        _.db_name, user=_.db_user, password=_.db_password,
        host=_.db_host, port=_.db_port
    )


database = create_database_from_settings(DB_SETTINGS, PostgresqlExtDatabase)
