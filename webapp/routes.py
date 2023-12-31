from flask import Blueprint, request,jsonify
import os

from app.controllers.HomeController import *

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home_route():
    return home()

@main.route('/predict', methods=['POST'])
def predict_route():
    return home_predict(request.get_json())

@main.route('/<path:undefined_path>', methods=['GET'])
def other_route(undefined_path):
    return home()
