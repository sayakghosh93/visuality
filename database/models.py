from database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user = None


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', backref=db.backref('Document', lazy='dynamic'))

    def __init__(self, user_id, file_path, id):
        self.user_id = user_id
        self.file_path = file_path
        self.id = id
        # self.user = user


class DocumentMetadata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey('document.id'))
    type = db.Column(db.String)
    data = db.Column(db.Text)

    def __init__(self, id, document_id, type, data):
        self.id = id
        self.document_id = document_id
        self.type = type
        self.data = data
