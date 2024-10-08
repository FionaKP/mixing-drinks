from flask import Blueprint, render_template
from app import db
from config import Config

errors_blueprint = Blueprint('errors', __name__)
errors_blueprint.template_folder = Config.TEMPLATE_FOLDER

@errors_blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('404error.html'), 404

@errors_blueprint.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500error.html'), 500