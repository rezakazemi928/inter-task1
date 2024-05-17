from fastapi import FastAPI
from app.helpers.d_1 import *
from app.helpers.d_2 import *
from uvicorn import run
router = FastAPI()

from tools import create_paginate_response


if __name__ == "__main__":
    run(router, host="0.0.0.0", port=8001)