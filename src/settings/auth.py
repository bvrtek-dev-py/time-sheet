import os
from dotenv import load_dotenv

load_dotenv()

ALGORITHM: str = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES: float = float(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
)
LOGIN_URL: str = "/api/v1/auth/login"
REFRESH_TOKEN_SECRET_KEY: str = os.getenv("REFRESH_TOKEN_SECRET_KEY")
SECRET_KEY: str = os.getenv("SECRET_KEY")
