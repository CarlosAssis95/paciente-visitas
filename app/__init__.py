from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from .routes.paciente_routes import paciente_bp
    from .routes.visitas_routes import visitas_bp
    app.register_blueprint(paciente_bp)
    app.register_blueprint(visitas_bp)

    return app
    