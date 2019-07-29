from flask import redirect, render_template, request, url_for
from flaskps.db import get_db
from flaskps.models.user import User


def index():
    User.db = get_db()
    users = User.all()

    return render_template('user/index.html', users=users)


def new():
    return render_template('user/new.html')


def create():
    User.db = get_db()
    User.create(request.form)
    return redirect(url_for('user_index'))

