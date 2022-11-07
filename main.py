from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from forms import CreatePostForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "Sas!@XZC098vcxlXS"
# Configure databes
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)


# Projects database
class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    subtitle = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    technologies = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)

# with app.app_context():
#     db.create_all()

@app.route('/')
def home():
    # Gets all projects from projects table
    projects = Project.query.all()
    return render_template("index.html", projects=projects)

# giCreate new Project in database
@app.route('/add', methods=["GET", "POST"])
def add():
    form = CreatePostForm()
    if request.method == "POST":
        new_project = Project(
            title=request.form.get("project_title"),
            subtitle = request.form.get("subtitle"),
            description = request.form.get("description"),
            technologies = request.form.get("technologies"),
            link = request.form.get("link")
          )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)



