from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.controllers import map_controller

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(map_controller.router)