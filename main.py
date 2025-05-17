import uvicorn
from app import app
from app.core.config import PORT, HOST

if __name__ == '__main__':
    uvicorn.run(app, port=PORT, host=HOST)
