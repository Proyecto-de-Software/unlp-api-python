from os import path
from flask import Flask, render_template, g
from flaskps.resources import issue
from flaskps.resources import user
from flaskps.resources import auth
from flaskps.resources.api import issue as api_issue
from flaskps.config import Config

# Configuración inicial de la app
app = Flask(__name__)
app.config.from_object(Config)

# Autenticación
app.add_url_rule("/iniciar_sesion", 'auth_login', auth.login)
app.add_url_rule("/cerrar_sesion", 'auth_logout', auth.logout)
app.add_url_rule(
    "/autenticacion",
    'auth_authenticate',
    auth.authenticate,
    methods=['POST']
)

# Consultas
app.add_url_rule("/consultas", 'issue_index', issue.index)
app.add_url_rule("/consultas", 'issue_create', issue.create, methods=['POST'])
app.add_url_rule("/consultas/new", 'issue_new', issue.new)

# Usuarios
app.add_url_rule("/usuarios", 'user_index', user.index)
app.add_url_rule("/usuarios", 'user_create', user.create, methods=['POST'])
app.add_url_rule("/usuarios/new", 'user_new', user.new)

# API-rest
app.add_url_rule("/api/consultas", 'api_issue_index', api_issue.index)


@app.route("/")
def hello():
    return render_template('home.html')
