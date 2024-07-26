from typing import Any, Callable, Iterable, TypeAlias

from playhouse.shortcuts import model_to_dict

from logic.config import DEFAULT_PAGE_SIZE, FIRST_PAGE
from repository.repositories.bases import CRUDRepositoryBase, ModelObject
from repository.repositories.implementations import (
    DevicePeeWeeRepository,
    LocationPeeWeeRepository, UserPeeWeeRepository,
)
from utils.crud_protocol import CreatedObjectId, CRUDOperationsBase, OperationSucceeded

SerializedModel: TypeAlias = dict[str, Any]


class CRUDServiceBase(CRUDOperationsBase):
    repository: CRUDRepositoryBase
    model_to_dict_serializer: Callable[[ModelObject, ...], SerializedModel] = model_to_dict

    def __init__(
            self, repository: CRUDRepositoryBase = None,
            model_to_dict_converter: Callable[[ModelObject], SerializedModel] = None
    ) -> None:
        # use the attribute of the instance class
        # to allow convenient subclassing, with providing default repository
        self.repository = repository or self.__class__.repository
        if not self.repository:
            raise ValueError('repository must be either passed or set at a child class')
        self.model_to_dict_serializer = \
            model_to_dict_converter or self.__class__.model_to_dict_serializer
        if not self.repository:
            raise ValueError(
                'model_to_dict_serializer must be either passed or set at a child class'
            )

    async def get_object_by_id(self, object_id: int, **serializer_kwargs) -> SerializedModel:
        retrieved_object = await self.repository.get_object_by_id(object_id)
        # force async query object evaluation, because it is lazy but
        # fails if passed directly to model_to_dict_serializer
        retrieved_object = [_ for _ in retrieved_object][0]
        return self.model_to_dict_serializer(
            retrieved_object,
            **serializer_kwargs
        )

    async def add_object(self, **fields) -> CreatedObjectId:
        return await self.repository.add_object(**fields)

    async def get_objects(
            self, page_number: int = FIRST_PAGE,
            page_size: int = DEFAULT_PAGE_SIZE,
            **serializer_kwargs
    ) -> Iterable[SerializedModel]:
        return [
            self.model_to_dict_serializer(model, **serializer_kwargs) for model in
            await self.repository.get_objects(page_number, page_size)
        ]

    async def update_object(self, object_id: int, **fields) -> OperationSucceeded:
        return await self.repository.update_object(object_id, **fields)

    async def delete_object(self, object_id: int) -> OperationSucceeded:
        return await self.repository.delete_object(object_id)


class UserService(CRUDServiceBase):
    repository = UserPeeWeeRepository()


class DeviceService(CRUDServiceBase):
    repository = DevicePeeWeeRepository()


class LocationService(CRUDServiceBase):
    repository = LocationPeeWeeRepository()
