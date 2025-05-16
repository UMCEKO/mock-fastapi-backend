from fastapi import FastAPI
from core.config import PORT, HOST
import uvicorn
import api

app = FastAPI()

app.include_router(api.router)


if __name__ == '__main__':
    uvicorn.run(app, port=PORT, host=HOST)