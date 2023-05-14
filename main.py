from flask import request, make_response, redirect, render_template, session
import unittest
from app.modelsdb import db
from app import create_app

app = create_app()

# Python variables
todos = ["Buy coffe", "Store groceries", "Sleep early"]

# Create the first Route
@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/greetings/hello'))
    # response.set_cookie("user_ip", user_ip)

    #Instead of storing the ip in a cookie, we will store it in a session
    session["user_ip"] = user_ip
    return response

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def not_found(error):
    return render_template('500.html', error=error)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)