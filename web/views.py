from logic.services import DeviceService
from web.crud_base_view import CRUDViewBase


class DeviceCRUDView(CRUDViewBase):
    service = DeviceService()
