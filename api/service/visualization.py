from database import db
from database.models import Visualization, VisualizationMetadata, DocumentMetadata, Document
import pandas as pd


class VisualizationResponseModel():
    def __init__(self, id, document_id, type, data, metadata):
        self.id = id
        self.document_id = document_id
        self.type = type
        self.data = data
        self.metadata = metadata


def get_visualizations_by_document_id(document_id):
    visualizations = Visualization.query.filter(Visualization.document_id == document_id).all()
    for visualization in visualizations:
        metadatas = VisualizationMetadata.query.filter(VisualizationMetadata.visualization_id == visualization.id)
        visualization.visualization_metadata = metadatas

    return visualizations


def create(document_id, data):
    data_ = data.get('data')
    type = data.get('type')
    visualization = Visualization(None, document_id, type, data_)

    db.session.add(visualization)
    db.session.commit()
    db.session.refresh(visualization)

    return visualization


def create_scatter_plot(document_id, df, features):
    feature_x = features[0]
    feature_y = features[1]
    data = []
    assert len(df[feature_x]) == len(df[feature_y])
    for _, row in df.iterrows():
        data.append({"x": row[feature_x], "y": row[feature_y]})

    visualization = Visualization(None, document_id, "scatter-plot", "")
    db.session.add(visualization)
    db.session.commit()
    db.session.refresh(visualization)
    visualization_metadata = VisualizationMetadata(None, visualization.id, str(data))
    db.session.add(visualization_metadata)
    db.session.commit()
    db.session.refresh(visualization_metadata)

    return VisualizationResponseModel(visualization.id, visualization.document_id, visualization.type,
                                      visualization.data, visualization_metadata)


def create_bar_plot(df, features):
    pass


def create_visualization_from_features(document_id, visualization_type, features):
    document = Document.query.filter(Document.id == document_id).one()
    # document_metadata_features = DocumentMetadata.query.filter(
    #     DocumentMetadata.document_id == document_id and (DocumentMetadata.type == 'features')).first()
    # for feature in features:
    #     if feature not in document_metadata_features:
    #         return "Feature not found"

    df = pd.read_csv(document.file_path, index_col=0)
    if visualization_type == 'scatter-plot':
        return create_scatter_plot(document_id, df, features)
    elif visualization_type == 'bar-plot':
        return create_bar_plot(document_id, df, features)


def add_metadatas(document_id, visualization_id, data):
    result = []
    for dat in data:
        data_ = dat.get('data')
        vis_metadata = VisualizationMetadata(None, visualization_id, data_)
        db.session.add(vis_metadata)
        db.session.commit()
        db.session.refresh(vis_metadata)
        result.append(vis_metadata)
    return result


def get_visualizations_by_document_id_type(document_id, type):
    visualization = Visualization.query.filter(
        Visualization.document_id == document_id and (Visualization.type == type)).one()

    return visualization
