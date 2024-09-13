from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

def create_app():
    # Load environment variables from the .env file
    load_dotenv()  # This loads the .env file and makes variables available via os.getenv()

    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes

    # Register your blueprint
    from .routes import main
    app.register_blueprint(main)

    return app