from flask import jsonify
from flaskps.db import get_db
from flaskps.models.issue import Issue


def index():
    Issue.db = get_db()
    issues = Issue.all()

    return jsonify(issues=issues)
