import pymysql

from flask import current_app, g
from flask.cli import with_appcontext
from flaskps.config import Config


def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASS,
            db=Config.DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
