from json import JSONDecodeError
from typing import Any, TypeAlias

from aiohttp.web_exceptions import HTTPBadRequest
from aiohttp.web_request import Request
from aiohttp.web_response import json_response
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

    def __init__(self, request: Request, service: CRUDServiceBase = None) -> None:
        super().__init__(request)
        self.service = service or self.__class__.service
        if not self.service:
            raise ValueError('service must be either passed or set at a child class')

    async def get(self):
        """provides a list of objects"""
        data_from_user = await self.__get_request_json()
        if page_number := self.__get_page_number(data_from_user):
            page_size = self.__get_page_size(data_from_user)
            return await self.service.get_objects(page_number, page_size)
        return json_response(await self.service.get_objects())

    async def post(self):
        """create an objects"""
        data_from_user = await self.__get_request_json()
        created_object_id = await self.service.add_object(**data_from_user)
        return json_response({'success': f'Successfully created, id: {created_object_id}'})

    async def delete(self):
        """delete an object"""
        data_from_user = await self.__get_request_json()
        object_id_to_delete = self.__get_object_id(data_from_user)
        deleted = await self.service.delete_object(object_id_to_delete)
        if deleted:
            return json_response({'success': f'Successfully deleted, id: {object_id_to_delete}'})
        raise FailedToDeleteObject

    async def patch(self):
        """update an object"""
        data_from_user = await self.__get_request_json()
        object_id_to_update = self.__get_object_id(data_from_user)
        data_without_object_id = {
            key: value for key, value in data_from_user.items()
            if key != CommonQueryParameters.OBJECT_ID
        }
        updated = await self.service.update_object(
            object_id_to_update, **data_without_object_id
        )
        if updated:
            return json_response({'success': 'Successfully updated'})
        raise FailedToUpdateObject

    async def __get_request_json(self) -> Json:
        try:
            return await self.request.json()
        except (JSONDecodeError, TypeError, UnicodeDecodeError) as e:
            raise HTTPBadRequest(reason='failed to parse data to json') from e

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
