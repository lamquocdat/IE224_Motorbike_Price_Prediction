from flask import Flask
from routes import main
import os

def create_app():
    template_dir = os.path.abspath('templates')
    static_dir = os.path.abspath('static')
    
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

    # Đăng ký các routes cho ứng dụng
    app.register_blueprint(main)

    return app
