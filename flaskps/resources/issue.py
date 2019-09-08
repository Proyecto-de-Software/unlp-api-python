from flask import redirect, render_template, request, url_for
from flaskps.db import get_db
from flaskps.models.issue import Issue


def index():
    Issue.db = get_db()
    issues = Issue.all()

    return render_template('issue/index.html', issues=issues)


def new():
    return render_template('issue/new.html')


def create():
    Issue.db = get_db()
    Issue.create(request.form)

    return redirect(url_for('issue_index'))
