from flask import redirect, render_template, request, url_for, session, abort
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.helpers.auth import authenticated


def index():
    if not authenticated(session):
        abort(401)

    User.db = get_db()
    users = User.all()

    return render_template('user/index.html', users=users)


def new():
    if not authenticated(session):
        abort(401)

    return render_template('user/new.html')


def create():
    if not authenticated(session):
        abort(401)

    User.db = get_db()
    User.create(request.form)
    return redirect(url_for('user_index'))
