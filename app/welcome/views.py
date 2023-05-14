from . import greetings
from flask import render_template, session, flash, redirect, url_for
from flask_login import login_required, current_user
from app.forms import ToDo, Delete
from app.queries import get_user, insert_task, delete_task, get_tasks, update_task


@greetings.route('/hello', methods=["GET", "POST"])
@login_required
def hello():
    # Ip of the user
    user_ip = session.get("user_ip")
    username = current_user.id
    todo_form = ToDo()
    
    context = {
        'user_ip': user_ip,
        "username": username,
        "todos": get_tasks(),
        "todo_form": todo_form
    }

    if todo_form.validate_on_submit():
        user = get_user(username)
        insert_task(todo_form.description.data, user.id)

        flash('Your task has been created succesfully!', category="success")

        return redirect(url_for('greetings.hello'))
    # the double ** is to pass the dictionary as kwargs
    return render_template('hello.html', **context)

@greetings.route("/tasks/delete/<task_id>", methods=["POST", "GET"])
def delete(task_id):
    delete_task(task_id)

    return redirect(url_for('greetings.hello'))

@greetings.route("/tasks/update/<task_id>/<int:done>", methods=["POST", "GET"])
def update(task_id, done):
    update_task(task_id, done)
    return redirect(url_for('greetings.hello'))
