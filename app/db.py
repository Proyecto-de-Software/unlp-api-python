import pymysql

from os import environ
from config import config


def connection():
    conf = config[environ.get('FLASK_ENV', 'development')]
    return pymysql.connect(
            host=conf.DB_HOST,
            user=conf.DB_USER,
            password=conf.DB_PASS,
            db=conf.DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )

