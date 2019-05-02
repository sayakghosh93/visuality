from api.restplus import api
from flask import request
from flask_restplus import Resource
from api.swagger import visualization_model
from api.swagger import visualization_metadata_model
from api.swagger import visualization_request

ns = api.namespace('v1/<int:document_id>/visualize/', description='Operations related to visualization')


@ns.route('/<string:visualization_type>')
@api.response(404, 'Document not found.')
class VisualizationItem(Resource):
    @api.expect(visualization_request)
    @api.marshal_with(visualization_model)
    def post(self, id):
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
        return None


@ns.route('/<string:visualization_type>/<int:visualization_id>')
@api.response(404, 'Visualization not found.')
class VisualizationItemView(Resource):
    @api.marshal_with(visualization_metadata_model)
    def get(self, id):
        """
        Returns a example.
        """
        return None
