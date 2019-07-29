from os import getenv
from importlib import import_module

def get_config():
  try:
      mode = getenv('FLASK_ENV', 'development')
      module = __name__ + "." + mode
      config = import_module(module)
      config.ENV = mode
      return config
  except ModuleNotFoundError:
      print(f"Configuration {module} is missing")
      exit(1)