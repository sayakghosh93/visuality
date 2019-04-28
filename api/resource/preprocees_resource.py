from api.restplus import api
from flask import request
from flask_restplus import Resource
from api.swagger import preprocessed_model

ns = api.namespace('v1/preprocess', description='Operations related to preprocessing the input data')


@ns.route('/<int:document_id>')
@api.response(404, 'Document not found.')
class PreprocessItem(Resource):

    @api.marshal_with(preprocessed_model)
    def post(self, id):
        """
        Returns a example.
        """
        return None
