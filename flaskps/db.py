import sqlite3

from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            '/home/fedeotaran/Documents/code/py_layout/db/db.sqlite',
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('/home/fedeotaran/Documents/code/py_layout/db/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

