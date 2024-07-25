from abc import ABC, abstractmethod
from typing import Iterable

from repository.types import UserID
from repository.schemas import UserSchema


class UserRepositoryBase(ABC):

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> UserSchema:
        ...

    @abstractmethod
    async def add_user(self, email: str, raw_password: str) -> UserID:
        ...

    @abstractmethod
    async def get_users(self, page_number: int, page_size: int) -> Iterable[UserSchema]:
        ...

    @abstractmethod
    async def update_user(self, user_id: int, **fields) -> bool:
        ...

    @abstractmethod
    async def delete_user(self, user_id: int) -> bool:
        ...
