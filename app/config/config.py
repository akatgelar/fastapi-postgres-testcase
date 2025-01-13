import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    
    PROJECT_NAME = "FastAPI Postgres TestCase"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
    ALGORITHM = "HS256"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

config = Config()

 