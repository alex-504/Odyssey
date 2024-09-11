from flask import Flask

def create_app():
    # Initialize the Flask app and specify the template folder
    app = Flask(__name__, template_folder='templates')

    # Register your blueprint
    from .routes import main
    app.register_blueprint(main)

    return app