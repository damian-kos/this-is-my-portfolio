from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email

# Form to add projects
class CreatePostForm(FlaskForm):
    project_title = StringField("Project title")
    subtitle = StringField("Project subtitle")
    description = StringField("Description")
    technologies = StringField("Technologies used")
    link = StringField("Projects URL(eg. on github)", validators=[DataRequired(), URL()])
    submit = SubmitField("Submit project")
