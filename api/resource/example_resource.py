from api.restplus import api
from flask import request
from flask_restplus import Resource
from api.swagger import example

ns = api.namespace('v1/example', description='Operations related to example resource')


@ns.route('/<int:id>')
@api.response(404, 'Example not found.')
class ExampleItem(Resource):

    @api.marshal_with(example)
    def get(self, id):
        """
        Returns a example.
        """
        return None

    @api.expect(example)
    @api.response(204, 'Example successfully updated.')
    def put(self, id):
        """
        Updates a example.
        Use this method to change the example.
        * Send a JSON object with the new name in the request body.
        ```
        {
          "name": "New Example Name"
        }
        ```
        * Specify the ID of the example to modify in the request URL path.
        """

        return None, 204

    @api.response(204, 'Example successfully deleted.')
    def delete(self, id):
        """
        Deletes example
        """
        return None, 204
