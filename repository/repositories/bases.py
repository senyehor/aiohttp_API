from abc import ABC, abstractmethod


class CRUDRepositoryBase(ABC):
    @abstractmethod
    async def get_object_by_id(self, object_id: int):
        ...

    @abstractmethod
    async def add_object(self, **fields):
        ...

    @abstractmethod
    async def get_objects(self, page_number: int, page_size: int):
        ...

    @abstractmethod
    async def update_object(self, object_id: int, **fields) -> bool:
        ...

    @abstractmethod
    async def delete_object(self, object_id: int) -> bool:
        ...
