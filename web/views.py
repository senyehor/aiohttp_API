from aiohttp.web_request import Request
from aiohttp.web_response import json_response

from logic.services import DeviceService
from web.crud_base_view import CRUDViewBase
from web.router import router


@router.view('/devices')
class DeviceCRUDView(CRUDViewBase):
    service = DeviceService()
