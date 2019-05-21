from api.restplus import api
from flask import request
from flask_restplus import Resource
from api.swagger import visualization_model, visualization_response_model, visualization_request
from api.swagger import visualization_metadata_model

from api.service import visualization as visualization_service

ns = api.namespace('v1/<int:document_id>/visualize/', description='Operations related to visualization')


@ns.route('/<string:visualization_type>')
@api.response(404, 'Document not found.')
class VisualizationItem(Resource):
    @api.expect(visualization_request)
    @api.marshal_with(visualization_response_model)
    def post(self, document_id, visualization_type):
        """
        Requests for a new visualization
        Use this method to change the example.
        * Send a JSON object with the new name in the request body.
        ```
        {
          "features": ["feature1","feature2"]
        }
        ```
        * Specify the ID of the example to modify in the request URL path.
        """
        data = request.json
        features = data.get('features')

        return visualization_service.create_visualization_from_features(document_id, visualization_type, features), 201


@ns.route('/<string:visualization_type>/<int:visualization_id>')
@api.response(404, 'Visualization not found.')
class VisualizationItemView(Resource):
    @api.marshal_with(visualization_metadata_model)
    def get(self, id):
        """
        Returns a example.
        """
        return None
