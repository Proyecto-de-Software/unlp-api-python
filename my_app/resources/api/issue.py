from flask import jsonify
from my_app.db import get_db
from my_app.models.issue import Issue


def index():
    Issue.db = get_db()
    issues = Issue.all()

    return jsonify(issues=issues)
