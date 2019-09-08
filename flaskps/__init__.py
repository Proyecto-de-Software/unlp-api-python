from os import path
from flask import Flask, render_template, g
from flaskps.resources import issue
from flaskps.config import get_config
from flaskps.resources import user
from flaskps.resources import auth

config = get_config()

# Configuración inicial de la app
app = Flask(__name__)
app.config.from_object(config)

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
