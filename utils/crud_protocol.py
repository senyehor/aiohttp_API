from abc import ABC, abstractmethod
from typing import Generic, Iterable, TypeAlias, TypeVar

ModelObject = TypeVar('ModelObject')
CreatedObjectId: TypeAlias = int


class CRUDOperationsBase(ABC, Generic[ModelObject]):
    @abstractmethod
    async def get_object_by_id(self, object_id: int) -> ModelObject:
        ...

    @abstractmethod
    async def add_object(self, **fields) -> CreatedObjectId:
        ...

    @abstractmethod
    async def get_objects(self, page_number: int, page_size: int) -> Iterable[ModelObject]:
        ...

    @abstractmethod
    async def update_object(self, object_id: int, **fields) -> bool:
        ...

    @abstractmethod
    async def delete_object(self, object_id: int) -> bool:
        ...
