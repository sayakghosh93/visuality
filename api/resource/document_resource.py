from api.restplus import api
from flask import request
from flask_restplus import Resource
from api.swagger import document
from api.swagger import document_metadata

from api.service import document as document_service
from flask_restplus import fields

ns = api.namespace('v1', description='Operations related to viewing the data')


@ns.route('/user/<int:user_id>/document')
@api.response(404, 'Document not found.')
class DocumentPostItem(Resource):
    @api.response(201, 'Document successfully created.')
    @api.marshal_with(document)
    @api.expect(document)
    def post(self, user_id):
        """
        Creates a new blog category.
        """
        data = request.json
        return document_service.create(user_id, data), 201


@ns.route('/user/<int:user_id>/document/<int:document_id>')
@api.response(404, 'Document not found.')
class DocumentGetItem(Resource):
    @api.marshal_with(document)
    def get(self, user_id, document_id):
        """
        Returns a example.
        """
        return document_service.get_document_by_id(document_id)


@ns.route('/user/<int:user_id>/document/<int:document_id>/metadata')
@api.response(404, 'Document not found.')
class DocumentMetadataCollection(Resource):
    @api.response(201, 'Document Metadata successfully created.')
    @api.marshal_list_with(document_metadata)
    @api.expect([document_metadata])
    def post(self, user_id, document_id):
        """
        Creates a new blog category.
        """
        data = request.json
        return document_service.add_metadatas(user_id, document_id, data), 201

    @api.marshal_list_with(document_metadata)
    def get(self, user_id, document_id):
        """
        Returns a example.
        """
        return document_service.get_metadatas(user_id, document_id)


@ns.route('/user/<int:user_id>/document/<int:document_id>/metadata/<int:document_metadata_id>')
@api.response(404, 'Document not found.')
class DocumentMetadataItem(Resource):
    @api.marshal_with(document_metadata)
    def get(self, user_id, document_id, document_metadata_id):
        """
        Returns a example.
        """
        return document_service.get_metadata(user_id, document_id, document_metadata_id)
