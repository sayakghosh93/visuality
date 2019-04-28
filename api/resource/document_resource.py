from api.restplus import api
from flask import request
from flask_restplus import Resource
from api.swagger import document

ns = api.namespace('v1', description='Operations related to viewing the data')


@ns.route('/<int:document_id>')
@api.response(404, 'Document not found.')
class DocumentItem(Resource):

    @api.marshal_with(document)
    def get(self, id):
        """
        Returns a example.
        """
        return None
