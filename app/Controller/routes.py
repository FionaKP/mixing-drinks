from flask import Blueprint, render_template, flash, redirect, url_for, request
from app import db
from config import Config

# from app.Controller.forms import CreatePositionForm, EditPositionForm, CreateApplicationForm, StatusForm, StudentEditForm, FacultyEditForm
# from app.Model.models import Position, Application, Faculty, Student, Status, Applied, User

routes_blueprint = Blueprint('routes', __name__)
routes_blueprint.template_folder = Config.TEMPLATE_FOLDER

@routes_blueprint.route('/', methods=['GET'])
@routes_blueprint.route('/index', methods=['GET'])
def index():
    return render_template('index.html')