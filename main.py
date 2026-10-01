from fastapi import FastAPI
from API.folders import router as folder_router

app = FastAPI()

app.include_router(folder_router)