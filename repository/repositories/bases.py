from abc import ABC, abstractmethod
from typing import Generic, Iterable, TypeVar

M = TypeVar('M')


class CRUDRepositoryBase(ABC, Generic[M]):
    def __init__(self, model_class: type[M]):
        # pylint: disable=unused-private-member
        self._model_class = model_class

    @abstractmethod
    async def get_object_by_id(self, object_id: int) -> M:
        ...

    @abstractmethod
    async def add_object(self, **fields):
        ...

    @abstractmethod
    async def get_objects(self, page_number: int, page_size: int) -> Iterable[M]:
        ...

    @abstractmethod
    async def update_object(self, object_id: int, **fields) -> bool:
        ...

    @abstractmethod
    async def delete_object(self, object_id: int) -> bool:
        ...
