from typing import Iterable

from peewee_async import execute

from repository.repositories.bases import CRUDRepositoryBase, ModelObject
from utils.crud_protocol import CreatedObjectId, OperationSucceeded


class PeeWeeCRUDRepository(CRUDRepositoryBase):
    """
    this is purely a layer between logic and database,
    no validation or error handling is done here
    """

    async def get_object_by_id(self, object_id: int) -> ModelObject:
        return await execute(
            self.model_class
            .select()
            .where(self.model_class.id == object_id)
        )

    async def add_object(self, **fields) -> CreatedObjectId:
        return await execute(
            self.model_class.insert(**fields)
        )

    async def get_objects(self, page_number: int, page_size: int) -> Iterable[ModelObject]:
        return await execute(
            self.model_class
            .select()
            .paginate(page_number, page_size)
        )

    async def update_object(self, object_id: int, **fields) -> OperationSucceeded:
        updated_object_id = await execute(
            self.model_class
            .update(**fields)
            .where(id=object_id)
        )
        return bool(updated_object_id)

    async def delete_object(self, object_id: int) -> OperationSucceeded:
        deleted_object_id = await execute(
            self.model_class
            .delete()
            .where(self.model_class.id == object_id)
        )
        return bool(deleted_object_id)
