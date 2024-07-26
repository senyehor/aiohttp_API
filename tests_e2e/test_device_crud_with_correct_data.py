import pytest
from aiohttp.test_utils import TestClient
from peewee_async import execute

from db.models import Device
from repository.schemas import DeviceSchema, LocationSchema, UserSchema
from tests_e2e.utils import device_to_dict

DEVICES_API_PATH = '/devices'


@pytest.mark.asyncio
class TestDeviceCRUD:

    async def test_create_device(
            self, test_client: TestClient, device: DeviceSchema,
            user_committed: UserSchema, location_committed: LocationSchema,
    ):
        device_data_correct = device_to_dict(device, user_committed, location_committed)
        response = await test_client.post(
            DEVICES_API_PATH,
            json=device_data_correct,
        )
        assert response.status == 200, 'wrong response code'
        device = await execute(
            Device
            .select()
            .where(
                Device.owner == user_committed,
                Device.location == location_committed,
                Device.login == device.login,
                Device.password == device.password,
            )
        )
        assert len(device) == 1, 'device was not created'
