from peewee_asyncext import PostgresqlExtDatabase

from config import DB_SETTINGS

_ = DB_SETTINGS
database = PostgresqlExtDatabase(
    _.db_name, user=_.db_user, password=_.db_password,
    host=_.db_host, port=_.db_port
)
