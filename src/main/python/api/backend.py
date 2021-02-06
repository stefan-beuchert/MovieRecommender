import flask
from flask_wtf.csrf import CSRFProtect

import config as conf
from in_out import connect_to_db, add_new_data_to_db, get_data, delete_data_from_db
from preparation.data_preparation import upload_raw_data
from processing.data_processing import process_data
from modeling.model_training import create_model, get_recommendation

app = flask.Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True
app.config["DEBUG"] = True

csrf = CSRFProtect(app)


def init(raw_data=None):
    global processed_data
    global model

    if raw_data is None:
        raw_data = get_data(db[conf.COLLECTION_RAW_DATA])
    processed_data = process_data(raw_data,
                                  db[conf.COLLECTION_PROCESSED_DATA],
                                  conf.DATA_COLUMNS,
                                  conf.TARGET_FEATURE,
                                  conf.UNWANTED_CHARACTERS,
                                  conf.STOP_WORD_LANGUAGE)
    model = create_model(processed_data, conf.TARGET_FEATURE)


@app.route('/', methods=['GET'])
def home():
    return "API is working"


@app.route('/getRecommendationFor/<label>', methods=['GET'])
def make_recommendation_from_get_request(label):
    return get_recommendation(label, model, processed_data, conf.LABEL_FEATURE)


@app.route('/getRecommendation/', methods=['POST'])
def make_recommendation_from_post_request():
    req_body = flask.request.get_json()
    label = req_body[conf.REQUEST_LABEL]
    return get_recommendation(label, model, processed_data, conf.LABEL_FEATURE)


@app.route('/addDataSet/', methods=['POST'])
def add_data_set():
    req_body = flask.request.get_json()
    new_data = {conf.LABEL_FEATURE: req_body[conf.REQUEST_LABEL], conf.TARGET_FEATURE: req_body[conf.REQUEST_TARGET]}

    add_new_data_to_db(db[conf.COLLECTION_RAW_DATA], new_data)

    init()

    return {"status": "data has been inserted"}


@app.route('/deleteDataSet/', methods=['DELETE'])
def delete_data_set():
    req_body = flask.request.get_json()
    data_label = req_body[conf.REQUEST_LABEL]

    delete_data_from_db(db[conf.COLLECTION_RAW_DATA], conf.LABEL_FEATURE, data_label)

    init()

    return {"status": "data has been deleted"}


db = connect_to_db(conf.DATABASE_URL, conf.DATABASE_NAME)
processed_data = None
model = None
init(upload_raw_data(conf.PATH_RAW_DATA, db[conf.COLLECTION_RAW_DATA]))

