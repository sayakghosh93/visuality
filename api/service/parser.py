from flask_restplus import reqparse
from werkzeug.datastructures import FileStorage

file_upload = reqparse.RequestParser()
file_upload.add_argument('file',
                         type=FileStorage,
                         location='files',
                         required=True,
                         help='CSV file')
