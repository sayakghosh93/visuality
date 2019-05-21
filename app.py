from flask import Flask, Blueprint
import settings
from api.restplus import api
# from api.resource.example_resource import ns as example_namespace
from api.resource.document_resource import ns as document_namespace
from api.resource.preprocees_resource import ns as preprocess_namespace
from api.resource.visualization_resource import ns as visualization_namespace
from api.resource.upload_resource import ns as upload_namespace

from database import db

# try:
#     from flask.ext.cors import CORS  # The typical way to import flask-cors
# except ImportError:
#     # Path hack allows examples to be run without installation.
#     import os
#
#     parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     os.sys.path.insert(0, parentdir)
#
#     from flask.ext.cors import CORS

app = Flask(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/api')


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['CORS_HEADERS'] = 'Content-Type'


def initialize_app(flask_app):
    configure_app(flask_app)

    api.init_app(blueprint)
    api.add_namespace(preprocess_namespace)
    api.add_namespace(document_namespace)
    api.add_namespace(visualization_namespace)
    api.add_namespace(upload_namespace)

    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)


def main():
    initialize_app(app)
    print('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)


# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')

@blueprint.after_request  # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header["Access-Control-Allow-Headers"] = "*"
    header["Access-Control-Allow-Methods"] = "*"
    return response


if __name__ == "__main__":
    main()
