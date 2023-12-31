from flask import render_template, jsonify
from app.services.old_motobike_predict import *
import joblib

encoder_path = 'app/utils/encoder.joblib'
model_path = 'app/models/random_forest.joblib'
encoder = joblib.load(encoder_path)
model = joblib.load(model_path)

def home():
    data = "hello"
    return render_template('index.html', **locals())

def home_predict(data):
    predict = predict_data(data, encoder, model)

    result = {
        "result": predict
    }

    return jsonify(result)