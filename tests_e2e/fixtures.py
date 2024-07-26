import pytest
import pytest_asyncio
from pytest_aiohttp.plugin import aiohttp_client

from db.for_test_only import _flush_db, _setup_test_db, _teardown_test_db
from db.models import Location, User
from main import create_app
from repository.tests.factories import DeviceFactory, LocationFactory, UserFactory


@pytest.fixture(scope='module')
def create_test_db():
    _setup_test_db()
    yield
    _teardown_test_db()


@pytest_asyncio.fixture(autouse=True, scope='function')
async def flush_db():
    yield
    await _flush_db()


@pytest_asyncio.fixture(scope='module')
async def client():
    app = await create_app()
    return await aiohttp_client(app)


@pytest.fixture()
def user():
    return UserFactory()


@pytest.fixture()
def user_committed(user):
    return User.create(email=user.email, password=user.password)


@pytest.fixture()
def location():
    return LocationFactory()


@pytest.fixture()
def location_committed(location):
    return Location.create(name=location.name)


@pytest.fixture()
def device(user, location):
    return DeviceFactory(owner=user, location=location)
