from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

db = SQLAlchemy()
moment = Moment()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.static_folder = config_class.STATIC_FOLDER 
    app.template_folder = config_class.TEMPLATE_FOLDER

    db.init_app(app)
    moment.init_app(app)

    # blueprint registration
    from app.Controller.errors import errors_blueprint as errors
    app.register_blueprint(errors)
    from app.Controller.routes import routes_blueprint as routes
    app.register_blueprint(routes)

    if not app.debug and not app.testing:
        pass
        # ... no changes to logging setup

    return app