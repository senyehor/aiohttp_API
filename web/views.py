from aiohttp.web_request import Request
from aiohttp.web_response import json_response

from logic.services import DeviceService
from web.crud_base_view import CRUDViewBase
from web.router import router


@router.view('/devices')
class DeviceCRUDView(CRUDViewBase):
    service = DeviceService()


@router.get(r'/devices/{object_id:\d+}')
async def device_info(request: Request):
    service = DeviceService()
    device_id = int(request.match_info['object_id'])
    return json_response(await service.get_object_by_id(device_id))
