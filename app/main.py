import uvicorn
from fastapi import FastAPI
from . import api

app = FastAPI()




if __name__ == "__main__":
    uvicorn.run(app, port=3000, host="0.0.0.0")