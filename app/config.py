from app.password import Password

class Config:
    SECRET_KEY = Password().generate_password(10)
    DEBUG = True
    ENV = 'deployment'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:M%40ps5250864POST@localhost:5432/authentication'
    SQLALCHEMY_TRACK_MODIFICATIONS = False