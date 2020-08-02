import os


class BaseConfig(object):
    """Base configuration."""

    DEBUG = None
    DB_HOST = 'bd_name'
    DB_USER = 'db_user'
    DB_PASS = 'db_pass'
    DB_NAME = 'db_name'
    SECRET_KEY = 'secret'

    @staticmethod
    def configure(app):
        # Implement this method to do further configuration on your app.
        pass 


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASS = 'root'
    DB_NAME = 'proyecto'
    ENV = 'development'

class TestingConfig(BaseConfig):
    """Testing configuration."""

    TESTING = True
    DEBUG = True
    DB_HOST = ''
    DB_USER = ''
    DB_PASS = ''
    DB_NAME = ''
    ENV = 'testing'

class ProductionConfig(BaseConfig):
    """Production configuration."""

    DB_HOST = ''
    DB_USER = ''
    DB_PASS = ''
    DB_NAME = ''
    ENV = 'production'


config = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)
