from app.password import Password
import os
from dotenv import load_dotenv

class Config:
    SECRET_KEY = Password().generate_password(10)
    DEBUG = True
    ENV = 'deployment'
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False