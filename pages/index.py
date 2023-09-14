from flask import Blueprint, render_template
from . import index_bp

# Route and view function for the index page
@index_bp.route('/')
def index():
    # Define any variables you want to pass to the template
    # For example:
    title = "Welcome to My Portfolio"
    description = "Explore my projects and learn more about me."

    # Render the "index.html" template with the provided data
    return render_template('index.html', title=title, description=description)
