from database import db
from database.models import User


def get_user_by_id(id):
    user = User.query.filter(User.id == id).one()
    return user
