from typing import Iterable

from peewee import Model
from peewee_async import execute

from db.models import User
from repository.repositories.bases import UserRepositoryBase


class PeeWeeAPIUserRepository(UserRepositoryBase):
    """
    this is purely a layer between logic and database,
    no validation or error handling is done here
    """

    def __init__(self, user_model: type[Model]):
        self.__user_model = user_model

    async def get_user_by_id(self, user_id: int) -> User:
        return await execute(
            self.__user_model
            .select()
            .where(self.__user_model.id == user_id)
        )

    async def add_user(self, email: str, raw_password: str):
        return await execute(
            self.__user_model.insert(email=email, password=raw_password)
        )

    async def get_users(self, page_number: int, page_size: int) -> Iterable[User]:
        return await execute(
            self.__user_model
            .select()
            .paginate(page_number, page_size)
        )

    async def update_user(self, user_id: int, **fields):
        updated_user_id = await execute(
            self.__user_model
            .update(**fields)
            .where(id=user_id)
        )
        return bool(updated_user_id)

    async def delete_user(self, user_id: int) -> bool:
        deleted_user_id = await execute(
            self.__user_model
            .delete()
            .where(self.__user_model.id == user_id)
        )
        return bool(deleted_user_id)
