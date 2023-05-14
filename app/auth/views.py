from . import auth
from flask import render_template, session, flash, url_for, redirect
from flask_login import login_user, login_required, logout_user, current_user
from app.forms import LoginForm, SignUpForm
from app.queries import insert_user, get_user, insert_location, get_location
from app.password import Password
from app.models import UserData, UserModel

@auth.route('/signup', methods=["GET", "POST"])
def signup():
    signup_form = SignUpForm()
    context = {
        'signup_form': signup_form
    }

    if signup_form.validate_on_submit():
        flash('You have succesfully registered a new user', category="success")
        username = signup_form.username.data
        email = signup_form.email.data
        password = Password().encrypt_password(signup_form.password.data)
        city = signup_form.city.data
        country = signup_form.country.data
        location = get_location(city)
        if not location:
            insert_location(city, country)
            location = get_location(city)
        insert_user(username, email, password, location.id)
        session["username"] = username

        return redirect(url_for('greetings.hello'))
    
    return render_template('signup.html', **context)


@auth.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    context = {
        'login_form':login_form
    }

    if login_form.validate_on_submit():
        username =login_form.username.data
        email =login_form.email.data
        password = login_form.password.data

        user_doc = get_user(username)

        if current_user.is_authenticated:
            return redirect(url_for('greetings.hello'))

        if (user_doc is not None 
            and user_doc.username == username
            and user_doc.email == email):

            password_db = user_doc.password
            if Password().verify_the_password(password_db, password):
                user_data = UserData(username, email, password_db)
                user = UserModel(user_data)
                login_user(user)
                flash("The user was logged in succesfully", category="success")

                return redirect(url_for('greetings.hello'))
            else:
                flash('The user does not match', category="error")
        else:
            flash('The user does not exist', category="error")
        return redirect(url_for('index'))
    
    return render_template('login.html', **context)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Come back soon!")

    return redirect(url_for("auth.login"))