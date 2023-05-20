# Todo List Project
## V 1.0

This is a Flask project to create a to do list.

## Installation
Fisrtly, it is necesary to download the repository
```bash
git clone https://github.com/MauricioAliendre182/Flask-project.git
```
Secondly, enters to the directory of the project, create a virtual environment and access to it.

**NOTE**: the name for this example is **venv**
```bash
cd Flask-project
pip install venv
pip -m venv venv
source venv/Script/activate
```

Lately, install what we have on the **requirements.txt** file
```bash
pip install -r requirements.txt
```
## Usage
To use this project locally firstly we need to add the following lines to the file **config.py**

![Config Flask Local](https://github.com/RodrigoValda/TestTitanWordpress/assets/86843637/9eea1a85-5db0-437d-b6d3-b76b9f7eb1f0)

As this project is using **PostgreSQL** as database it is neccesary to configure it with local variables, for this you need to create a file called **.env**, this file will be placed on the folder **/app**, the path will be **/app/.env**, on this file we will annotate the database credentials as following:
```bash
SQLALCHEMY_DATABASE_URI=postgresql://username:password@host:port/database
```
Where:

- **username**: is the database username
- **password** is the password of database
- **host** is the host (for this case is **localhost**)
- **port**: is the port (generally is **5432** for PostgreSQL)
- **database**: is the database as such

Once configured this, you can go to **main.py** file and execute it, at the first execution the tables will be created in your database you will be able  to work with it

## Result
This project is shelter in [Render](https://dashboard.render.com/) you can see athe page in the [link](https://task-list-xi5k.onrender.com/auth/login?next=%2Fgreetings%2Fhello)

## License

This project is free an can be used for anyone
