from typing import Iterable

from peewee_async import execute

from repository.repositories.bases import CreatedObjectId, CRUDRepositoryBase, ModelObject


class PeeWeeCRUDRepository(CRUDRepositoryBase):
    """
    this is purely a layer between logic and database,
    no validation or error handling is done here
    """

    async def get_object_by_id(self, object_id: int) -> ModelObject:
        return await execute(
            self._model_class
            .select()
            .where(self._model_class.id == object_id)
        )

    async def add_object(self, **fields) -> CreatedObjectId:
        return await execute(
            self._model_class.insert(**fields)
        )

    async def get_objects(self, page_number: int, page_size: int) -> Iterable[ModelObject]:
        return await execute(
            self._model_class
            .select()
            .paginate(page_number, page_size)
        )

    async def update_object(self, object_id: int, **fields) -> bool:
        updated_object_id = await execute(
            self._model_class
            .update(**fields)
            .where(id=object_id)
        )
        return bool(updated_object_id)

    async def delete_object(self, object_id: int) -> bool:
        deleted_object_id = await execute(
            self._model_class
            .delete()
            .where(self._model_class.id == object_id)
        )
        return bool(deleted_object_id)
