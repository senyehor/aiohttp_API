import pytest
import pytest_asyncio

from db.for_test_only import _flush_db, _setup_test_db, _teardown_test_db


@pytest.fixture(scope='module')
def create_test_db():
    _setup_test_db()
    yield
    _teardown_test_db()


@pytest_asyncio.fixture(autouse=True, scope='function')
async def flush_db():
    yield
    await _flush_db()
