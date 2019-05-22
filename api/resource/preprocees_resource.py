from api.restplus import api
from flask import request
from flask_restplus import Resource
from api.swagger import preprocessed_model
from api.swagger import visualization_response_model
from api.service import proprocess as preprocess_service

ns = api.namespace('v1/preprocess', description='Operations related to preprocessing the input data')


@ns.route('/<int:document_id>')
@api.response(404, 'Document not found.')
class PreprocessItem(Resource):

    @api.marshal_list_with(visualization_response_model)
    def post(self, document_id):
        """
        Returns a example.
        """
        return preprocess_service.generate_visulalizations(document_id)
