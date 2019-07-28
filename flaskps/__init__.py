from os import path
from flask import Flask, render_template, g
from flaskps.db import init_db
from flaskps.resources import issue
from flaskps.resources import user
from flaskps.resources import auth

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=path.join("../db/db.sqlite"),
)

# Consultas
app.add_url_rule("/consultas", 'issue_index', issue.index)
app.add_url_rule("/consultas", 'issue_create', issue.create, methods=['POST'])
app.add_url_rule("/consultas/new", 'issue_new', issue.new)

# Usuarios
app.add_url_rule("/usuarios", 'user_index', user.index)
app.add_url_rule("/usuarios", 'user_create', user.create, methods=['POST'])
app.add_url_rule("/usuarios/new", 'user_new', user.new)

# Autenticación
app.add_url_rule("/iniciar_sesion", 'auth_login', auth.login)
app.add_url_rule(
    "/autenticacion",
    'auth_authenticate',
    auth.authenticate,
    methods=['POST']
)


@app.route("/")
def hello():
    return render_template('home.html')


@app.cli.command('initdb')
def initdb_command():
    print("Init db start!")
    init_db()
    print("Init db done!")


