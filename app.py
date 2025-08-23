from flask import Flask, render_template
import data_layer

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
json_data = str(BASE_DIR / "data.json")

# Laddar in json data
projects_data = data_layer.load(json_data)

# Startar en flask app och säger att den ska kolla i templates mappen för templates
app = Flask(__name__, template_folder='./templates')

# Routing för "/"
@app.route("/")
@app.route("/Projects")
def projects_page():
    return render_template('projects.html', projects=projects_data)

# Routing för "/About"
@app.route("/About")
def about_page():
    return render_template('about.html', projects=projects_data)

# Routing för "/Project"
@app.route("/project/<int:project_id>")
def project_detail(project_id):
    # Hitta projektet i JSON/listan
    project = next((p for p in projects_data if p["project_id"] == project_id), None)
    
    if project is None:
        return "Projektet finns inte", 404

    return render_template("project_detail.html", project=project)

# Kör programmet
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

"""
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
"""
