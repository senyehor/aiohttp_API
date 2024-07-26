from typing import Iterable

from repository.repositories.bases import CRUDRepositoryBase
from repository.repositories.implementations import (
    DevicePeeWeeRepository,
    LocationPeeWeeRepository, UserPeeWeeRepository,
)
from utils.crud_protocol import CreatedObjectId, CRUDOperationsBase, ModelObject


class CRUDServiceBase(CRUDOperationsBase):
    repository: CRUDRepositoryBase

    async def get_object_by_id(self, object_id: int) -> ModelObject:
        return await self.repository.get_object_by_id(object_id)

    async def add_object(self, **fields) -> CreatedObjectId:
        return await self.repository.add_object(**fields)

    async def get_objects(self, page_number: int, page_size: int) -> Iterable[ModelObject]:
        return await self.repository.get_objects(page_number, page_size)

    async def update_object(self, object_id: int, **fields) -> bool:
        return await self.repository.update_object(object_id, **fields)

    async def delete_object(self, object_id: int) -> bool:
        return await self.repository.delete_object(object_id)


class UserService(CRUDServiceBase):
    repository = UserPeeWeeRepository


class DeviceService(CRUDServiceBase):
    repository = DevicePeeWeeRepository


class LocationService(CRUDServiceBase):
    repository = LocationPeeWeeRepository
