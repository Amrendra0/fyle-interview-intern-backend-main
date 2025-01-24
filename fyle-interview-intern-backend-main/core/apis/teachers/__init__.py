from flask import Blueprint
from core.apis.teacher.principal import teacher_views

# Define Blueprint for teacher APIs
teacher_blueprint = Blueprint("teacher", __name__)

# Register teacher routes
teacher_blueprint.register_blueprint(teacher_views, url_prefix="/teacher")
