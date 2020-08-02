import pymysql

from flask import current_app
from flask import g
from flask import cli


def connection():
    if "db_conn" not in g:
        conf = current_app.config
        g.db_conn = pymysql.connect(
            host=conf["DB_HOST"],
            user=conf["DB_USER"],
            password=conf["DB_PASS"],
            db=conf["DB_NAME"],
            cursorclass=pymysql.cursors.DictCursor,
        )

    return g.db_conn


def close(e=None):
    conn = g.pop("db_conn", None)

    if conn is not None:
        conn.close()


def init_app(app):
    app.teardown_appcontext(close)
