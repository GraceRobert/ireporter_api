"""Initializes the flask app"""



from flask import Flask, jsonify
from flask_restful import Api
from app.v1.views import NewRedflags
from app.v1.views import GetRedflag
from app.v1.views import GetRedflags
from config import app_config

def create_app(config_name):

    """Factory initialization for the app"""

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])

    #app.config.from_pyfile('config.py')
    # Initialize flask_restful and add routes

    api_endpoint = Api(app)

    # Products Resource

    api_endpoint.add_resource(NewRedflags, '/api/v1/incidents')
    api_endpoint.add_resource(GetRedflags, '/api/v1/incidents')
    api_endpoint.add_resource(GetRedflag, '/api/v1/incidents/<int:redflag_id>')
    
    return app