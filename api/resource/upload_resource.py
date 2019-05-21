from api.restplus import api
from flask import request
from flask import make_response
from flask_restplus import Resource
import settings

from api.service import parser
import os
from api.service import file_uploader
from api.swagger import document_response_model

ns = api.namespace('v1/user/<int:user_id>', description='Operations related to uploading the data')


@ns.route('/upload')
@api.response(404, 'Upload Failed')
class Upload(Resource):
    @api.response(201, 'Upload successfuly done')
    @api.expect(parser.file_upload)
    @api.marshal_with(document_response_model)
    def post(self, user_id):
        args = parser.file_upload.parse_args()
        uploaded_file = args['file']

        status, document = file_uploader.upload_file(user_id, uploaded_file)
        if status:
            # response = make_response(document)
            # response.headers.add('Access-Control-Allow-Origin', '*')
            return document, 200
        else:
            return {'status': 'Failed'}, 400
