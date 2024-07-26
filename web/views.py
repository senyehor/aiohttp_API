from logic.services import DeviceService
from web.crud_base_view import CRUDViewBase
from web.routes import router


@router.view('/devices')
class DeviceCRUDView(CRUDViewBase):
    service = DeviceService()
