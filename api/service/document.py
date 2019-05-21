from database import db
from database.models import User, Document, DocumentMetadata
import pandas as pd


class DocumentResponseModel():
    def __init__(self, id, user_id, file_path, metadata):
        self.id = id
        self.user_id = user_id
        self.file_path = file_path
        self.metadata = metadata


def get_document_by_id(id):
    document = Document.query.filter(Document.id == id).one()
    return document


def create(user_id, data):
    file_path = data.get('file_path')

    document = Document(user_id, file_path, None)
    document = save_data(document)

    return document


def add_metadatas(user_id, document_id, data):
    result = []
    for dat in data:
        type = dat.get('type')
        data_ = dat.get('data')
        doc_metadata = DocumentMetadata(None, document_id, type, data_)
        doc_metadata = save_data(doc_metadata)
        result.append(doc_metadata)
    return result


def get_metadatas(user_id, document_id):
    metadatas = DocumentMetadata.query.filter(DocumentMetadata.document_id == document_id).all()
    return metadatas


def get_metadata(user_id, document_id, document_metadata_id):
    metadata = DocumentMetadata.query.filter(DocumentMetadata.id == document_metadata_id).one()
    return metadata


def find_feature_type(df, feature):
    feature_vals = df[feature]
    n = feature_vals.shape[0]
    unique = feature_vals.nunique()
    if (unique / n) < 0.1:
        return "categorical"
    return "ordinal"


def save_data(model):
    db.session.add(model)
    db.session.commit()
    db.session.refresh(model)
    return model


def label_features(df, features, document_id):
    numerical_features = []
    categorical_features = []

    for feature in features:
        feature_type = find_feature_type(df, feature)
        if feature_type == "categorical":
            categorical_features.append(feature)
        else:
            numerical_features.append(feature)
    document_metadata_cat = DocumentMetadata(None, document_id, "categorical_features", str(categorical_features))
    document_metadata_num = DocumentMetadata(None, document_id, "numerical_features", str(numerical_features))

    document_metadata_cat = save_data(document_metadata_cat)
    document_metadata_num = save_data(document_metadata_num)

    return [document_metadata_cat, document_metadata_num]


def find_document_metadata(document):
    metadatas = []
    df = pd.read_csv(document.file_path, index_col=0)
    features = list(df.columns)
    document_metadata = DocumentMetadata(None, document.id, "features", str(features))
    document_metadata = save_data(document_metadata)

    metadatas.append(document_metadata)
    metadatas.extend(label_features(df, features, document.id))
    return metadatas


def save_document(user_id, file_name):
    user = User.query.filter(User.id == user_id).one()
    file_path = 'data/' + user.username + '/' + file_name
    document = Document(user_id, file_path, None)
    document = save_data(document)
    metadatas = find_document_metadata(document)
    response = DocumentResponseModel(document.id, user_id, document.file_path, metadatas)
    return response
