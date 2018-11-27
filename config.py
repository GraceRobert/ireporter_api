"""The configuration for the app"""

import os

class Config(object):

    """Parent configuration class."""

    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')

class DevelopmentConfig(Config):

    """Configurations for Development."""

    DEBUG = True

class TestingConfig(Config):

    """Configurations for Testing"""
    TESTING = True
    DEBUG = True

app_config = {

    'development': DevelopmentConfig,
    'testing': TestingConfig

}


