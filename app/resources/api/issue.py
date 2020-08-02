from flask import jsonify
from app.db import connection
from app.models.issue import Issue


def index():
    conn = connection()
    issues = Issue.all(conn)

    return jsonify(issues=issues)
