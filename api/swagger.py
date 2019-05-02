from flask_restplus import fields
from api.restplus import api

example = api.model('Example', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of example'),
    'name': fields.String(required=True, description='example name'),
})

visualization_model = api.model('Visualization Model', {
    'visualization_id': fields.Integer(readOnly=True, description='The unique identifier of visualization object'),
    'visualization_type': fields.String(required=True, description='Type of visualization'),
})

preprocessed_model = api.model('Preprocessed Model', {
    'document_id': fields.Integer(readOnly=True, description='The unique identifier of document'),
    'visualizations': fields.List(fields.Nested(visualization_model))
    ,
})

feature = api.model('feature', {
    'name': fields.String(readOnly=True, description='The name of the feature'),
    'dtype': fields.String(required=True, description='data type of the feature'),
})

document = api.model('Document', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of document'),
    'type': fields.String(required=True, description='Type of document'),
    'features': fields.List(fields.Nested(feature))
})

visualization_request = api.model('Feature', {
    'features': fields.List(fields.String(readOnly=True, description='The name of the feature')),
})

visualization_status_model = api.model('Status', {
    'status': fields.String(readOnly=True, description='The status of the visualization'),
    'download_url': fields.String(required=True, description='download url of the visualization'),
})

visualization_metadata_model = api.model('Visualization Metadata Model', {
    'visualization_id': fields.String(readOnly=True, description='visualization id associated with the metadata'),
    'data': fields.String(required=True, description='Data required to render the visualization'),
})
