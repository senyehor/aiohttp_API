from pathlib import Path

from peewee import Database
from peewee_async import AsyncDatabase, execute

from config import DBSettings
from db.connection import create_database_from_settings, DEFAULT_DB_CREATOR
from db.models import Device, Location, User


class _DBTestOnlySettings(DBSettings):
    class Config:
        env_file = f'{Path(__file__).resolve().parent.parent}/test.env'
        env_file_encoding = 'utf-8'


_MODELS_ORDERED_TO_DROP_CORRECTLY = (Device, User, Location)
# this typehint allows to have correct suggestions, even though
# it is not supported to be used with a sync db
_TEST_DB: Database | AsyncDatabase = create_database_from_settings(
    _DBTestOnlySettings(),
    DEFAULT_DB_CREATOR
)


def _setup_test_db():
    """make models use the test db, create tables"""
    _TEST_DB.bind(
        _MODELS_ORDERED_TO_DROP_CORRECTLY,
        bind_refs=False, bind_backrefs=False
    )
    _TEST_DB.connect()
    _TEST_DB.create_tables(_MODELS_ORDERED_TO_DROP_CORRECTLY)


def _teardown_test_db():
    """drop tables and close db"""
    _TEST_DB.drop_tables(_MODELS_ORDERED_TO_DROP_CORRECTLY)
    _TEST_DB.close()


async def _flush_db():
    for model in _MODELS_ORDERED_TO_DROP_CORRECTLY:
        await execute(
            model
            .delete()
        )
