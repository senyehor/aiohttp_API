from typing import Any, TypeAlias

from aiohttp.web_request import Request
from aiohttp.web_response import Response
from aiohttp.web_urldispatcher import View

from logic.services import CRUDServiceBase
from web.exceptions import (
    FailedToDeleteObject, FailedToUpdateObject, ObjectIdNotFoundOrIncorrect, PageNumberIncorrect,
    PageSizeIncorrect,
)
from web.utils import CommonQueryParameters

Json: TypeAlias = dict[str, Any]


class CRUDViewBase(View):
    service: CRUDServiceBase

    async def get(self, request: Request):
        """provides a list of objects"""
        data_from_user = await request.json()
        if page_number := self.__get_page_number(data_from_user):
            page_size = self.__get_page_size(data_from_user)
            return self.service.get_objects(page_number, page_size)
        return await self.service.get_objects()

    async def post(self, request: Request):
        """create an objects"""
        data_from_user = await request.json()
        created_object_id = await self.service.add_object(**data_from_user)
        return Response(text=f'Successfully created, id: {created_object_id}')

    async def delete(self, request: Request):
        """delete an object"""
        data_from_user = await request.json()
        object_id_to_delete = self.__get_object_id(data_from_user)
        deleted = await self.service.delete_object(object_id_to_delete)
        if deleted:
            return Response(text='Successfully deleted')
        raise FailedToDeleteObject

    async def patch(self, request: Request):
        """update an object"""
        data_from_user: Json = await request.json()
        object_id_to_update = self.__get_object_id(data_from_user)
        data_without_object_id = {
            key: value for key, value in data_from_user.items()
            if key != CommonQueryParameters.OBJECT_ID
        }
        updated = await self.service.update_object(
            object_id_to_update, **data_without_object_id
        )
        if updated:
            return Response(text='Successfully updated')
        raise FailedToUpdateObject

    def __get_object_id(self, data_from_user: Json) -> int:
        return self.__get_required_int_from_user_data(
            data_from_user, CommonQueryParameters.OBJECT_ID,
            ObjectIdNotFoundOrIncorrect
        )

    def __get_page_number(self, data_from_user: Json) -> int | None:
        try:
            return int(data_from_user[CommonQueryParameters.PAGE_NUMBER])
        except KeyError:
            return None
        except ValueError as e:
            raise PageNumberIncorrect() from e

    def __get_page_size(self, data_from_user: Json) -> int:
        return self.__get_required_int_from_user_data(
            data_from_user, CommonQueryParameters.PAGE_SIZE,
            PageSizeIncorrect
        )

    def __get_required_int_from_user_data(
            self, data_from_user: Json, key: str,
            exception_to_raise: type[Exception]
    ) -> int:
        try:
            return int(data_from_user[key])
        except (ValueError, KeyError) as e:
            raise exception_to_raise() from e
