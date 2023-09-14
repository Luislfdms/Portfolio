from flask import Blueprint

# Create Blueprint instances for each page
index_bp = Blueprint('index', __name__)
about_bp = Blueprint('about', __name__, url_prefix='/about')
projects_bp = Blueprint('projects', __name__, url_prefix='/projects')
experience_bp = Blueprint('experience', __name__, url_prefix='/experience')
# Import views from individual modules to register them
from . import index, projects, about
