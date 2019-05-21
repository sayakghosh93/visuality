import os
import settings
from api.service import document as document_service
from database.models import User


def upload_file(user_id, uploaded_file):
    user = User.query.filter(User.id == user_id).one()

    if uploaded_file:
        destination = os.path.join(settings.DATA_PATH, 'data\\' + user.username)
        if not os.path.exists(destination):
            os.makedirs(destination)
        file_path = '%s%s' % (destination, uploaded_file.filename)

        uploaded_file.save(file_path)
        filename = uploaded_file.filename
        document = document_service.save_document(user_id, filename, file_path)
        return True, document
    else:
        return False, None
