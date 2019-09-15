from os import getenv
from importlib import import_module

# Función para recuperar la configuración dependiendo del entorno
def get_config():
  try:
      # Entorno por defecto si no se especifica otro, development
      mode = getenv('FLASK_ENV', 'development')
      module = __name__ + "." + mode
      config = import_module(module)
      config.ENV = mode
      return config
  except ModuleNotFoundError:
      print(f"Configuration {module} is missing")
      exit(1)

Config = get_config()
