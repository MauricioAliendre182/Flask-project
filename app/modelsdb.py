from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    def __init__(self, username, email, password, location):
        self.username = username
        self.email = email
        self.password = password
        self.id_location = location

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    id_location = db.Column(UUID(as_uuid=True), db.ForeignKey('locations.id'))
    task = db.relationship('Task', backref='tasks', lazy=True)

class Location(db.Model):
    __tablename__ = 'locations'
    def __init__(self, city, country):
        self.city = city
        self.country = country
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False)
    city = db.Column(db.String(25), nullable=False)
    country = db.Column(db.String(35), nullable=False)
    user = db.relationship('Users', backref='users', lazy=True)

class Task(db.Model):
    __tablename__ = 'tasks'
    def __init__(self, description, user):
        self.description = description
        self.id_user = user
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)
    id_user = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'))