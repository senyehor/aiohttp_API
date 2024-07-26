#!/bin/bash
gunicorn main:create_app --bind 0.0.0.0:$APP_PORT --worker-class aiohttp.GunicornWebWorker
