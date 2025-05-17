import os
from urllib.parse import urlparse

import dotenv

dotenv.load_dotenv(dotenv_path=".env", override=True)

# S3 Configuration

S3_ENDPOINT = os.getenv("S3_ENDPOINT")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
S3_BUCKET = os.getenv("S3_BUCKET")
S3_REGION = os.getenv("S3_REGION")

# Media url to be accessed from

MEDIA_URL = urlparse(os.getenv("MEDIA_URL", "http://localhost:3000"))

# Other

PORT = int(os.getenv("PORT", "3000"))
HOST = os.getenv("HOST", "0.0.0.0")