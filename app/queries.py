from .modelsdb import db, Users, Location, Task

def insert_user(username, email, password, location):
    user = Users(username, email, password, location)
    db.session.add(user)
    db.session.commit()

def delete_user(username):
    user = Users.query.filter_by(username).first()
    db.session.delete(user)
    db.session.commit()

def get_users():
    user = Users.query.all()
    return user

def get_user(username):
    user = Users.query.filter_by(username=username).first()
    return user

def insert_location(city, country):
    location = Location(city, country)
    db.session.add(location)
    db.session.commit()
    return location

def delete_location(city):
    location = Location.query.filter_by(city=city).first()
    db.session.delete(location)
    db.session.commit()

def get_location():
    location = Location.query.all()
    return location

def get_location(city):
    location = Location.query.filter_by(city=city).first()
    return location

def insert_task(task, user):
    task = Task(task, user)
    db.session.add(task)
    db.session.commit()
    return task

def delete_task(id):
    task = Task.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()

def get_tasks():
    task = Task.query.all()
    return task

def get_task(id):
    task = Task.query.filter_by(id=id).first()
    return task

def update_task(id, done):
    task = get_task(id)
    if done == 0:
        task.done = True
    else:
        task.done=False
    db.session.commit()