from flask import Flask, render_template
from pages import index, projects, about, experience

app = Flask(__name__)

# Register blueprints for different pages
app.register_blueprint(index.index_bp)
app.register_blueprint(projects.projects_bp)
app.register_blueprint(about.about_bp)
app.register_blueprint(experience.experience_bp)

if __name__ == '__main__':
    app.run(debug=True)
