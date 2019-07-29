from os import path
from flask import Flask, render_template, g
from flaskps.db import init_db
from flaskps.resources import issue
from flaskps.config import get_config

config = get_config()

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(issue.bp)

@app.route("/")
def hello():
    return render_template('home.html')

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()


@app.cli.command('initdb')
def initdb_command():
    print("Init db start!")
    init_db()
    print("Init db done!")


