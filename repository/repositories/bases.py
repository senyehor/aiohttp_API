from abc import ABC, abstractmethod
from typing import Generic, Iterable, TypeVar

from utils.crud_protocol import CreatedObjectId, CRUDOperationsBase, OperationSucceeded

ModelObject = TypeVar('ModelObject')


class CRUDRepositoryBase(CRUDOperationsBase, ABC, Generic[ModelObject]):
    model_class: type[ModelObject]

    @abstractmethod
    async def get_object_by_id(self, object_id: int) -> ModelObject:
        pass

    @abstractmethod
    async def add_object(self, **fields) -> CreatedObjectId:
        pass

    @abstractmethod
    async def get_objects(self, page_number: int, page_size: int) -> Iterable[ModelObject]:
        pass

    @abstractmethod
    async def update_object(self, object_id: int, **fields) -> OperationSucceeded:
        pass

    @abstractmethod
    async def delete_object(self, object_id: int) -> OperationSucceeded:
        pass
