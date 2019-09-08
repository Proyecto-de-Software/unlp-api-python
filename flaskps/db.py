import pymysql

from flask import current_app, g
from flask.cli import with_appcontext
from flaskps.config import get_config


def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(
            host=get_config().DB_HOST,
            user=get_config().DB_USER,
            password=get_config().DB_PASS,
            db=get_config().DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
