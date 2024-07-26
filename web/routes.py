from aiohttp.web_routedef import RouteTableDef

from web.views import DeviceCRUDView

router = RouteTableDef()

router.view('/devices')(DeviceCRUDView)
