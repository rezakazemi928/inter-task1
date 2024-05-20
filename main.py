from fastapi import FastAPI
from uvicorn import run

from backend.routers import router

app = FastAPI()
app.include_router(router=router)

if __name__ == "__main__":
    run(app="main:app", host="0.0.0.0", port=8001, reload=True)
