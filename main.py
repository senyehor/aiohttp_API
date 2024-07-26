import logging

from aiohttp.web import run_app
from aiohttp.web_app import Application

from config import DEBUG
from web.router import router


async def create_app():
    app = Application()
    app.add_routes(router)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler(), logging.FileHandler('.logs')]
    )
    if DEBUG:
        logging.basicConfig(level=logging.DEBUG)
    return app


if __name__ == '__main__':
    run_app(create_app())
