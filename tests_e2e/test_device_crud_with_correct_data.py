import pytest
from aiohttp.test_utils import TestClient
from peewee_async import execute

from db.models import Device
from logic.config import DEFAULT_PAGE_SIZE
from repository.schemas import DeviceSchema, LocationSchema, UserSchema
from repository.tests.factories import DeviceFactory
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

    async def test_retrieve_devices_default_pagination(
            self, test_client: TestClient, user_committed: UserSchema,
            location_committed: LocationSchema
    ):
        devices = self.create_and_insert_devices(13, user_committed, location_committed)
        response = await test_client.get(DEVICES_API_PATH)
        assert response.status == 200, 'wrong response code'
        content = await response.json()
        devices_on_page_ids = [device.id for device in devices[:DEFAULT_PAGE_SIZE]]
        devices_ids_received = [device['id'] for device in content]
        assert sorted(devices_on_page_ids) == sorted(devices_ids_received), \
            'received devices do not match expected'

    async def test_delete_device(
            self,
            test_client: TestClient, user_committed: UserSchema,
            location_committed: LocationSchema, device: DeviceSchema
    ):
        device = self.create_and_insert_devices(1, user_committed, location_committed)[0]
        response = await test_client.delete(DEVICES_API_PATH, json={'object_id': device.id})
        assert response.status == 200, 'wrong response code'
        device = await execute(
            Device
            .select()
            .where(Device.id == device.id)  # pylint: disable=no-member
        )
        assert len(device) == 0, 'device still present in database after deletion'

    def create_and_insert_devices(
            self, count: int, user: UserSchema, location: LocationSchema
    ) -> list[Device]:
        devices = []
        for _ in range(count):
            device = DeviceFactory(
                location=location,
                owner=user
            )
            device = Device.create(
                type=device.type, login=device.login, password=device.password,
                owner=user, location=location
            )
            devices.append(device)
        return devices
