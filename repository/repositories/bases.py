from abc import ABC, abstractmethod
from typing import Iterable

from repository.types import UserID
from repository.schemas import APIUser


class APIUserRepositoryBase(ABC):

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> APIUser:
        ...

    @abstractmethod
    async def add_user(self, email: str, raw_password: str) -> UserID:
        ...

    @abstractmethod
    async def get_users(self, page_number: int, page_size: int) -> Iterable[APIUser]:
        ...

    @abstractmethod
    async def update_user(self, user_id: int, **fields) -> bool:
        ...

    @abstractmethod
    async def delete_user(self, user_id: int) -> bool:
        ...
