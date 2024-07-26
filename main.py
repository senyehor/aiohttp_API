from aiohttp.web import run_app
from aiohttp.web_app import Application

from web.routes import router


async def create_app():
    app = Application()
    app.add_routes(router)
    return app


if __name__ == '__main__':
    run_app(create_app())
