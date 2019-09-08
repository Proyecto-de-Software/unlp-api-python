from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.user import User


def login():
    return render_template('auth/login.html')


def authenticate():
    params = request.form

    User.db = get_db()
    user = User.find_by_email_and_pass(params['email'], params['password'])

    if not user:
        abort(401)

    session['user'] = user['email']
    flash("La sesión se inició correctamente.")

    return redirect(url_for('issue_index'))
