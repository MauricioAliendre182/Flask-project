from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp
from .queries import insert_user

# Validator only works to check if for example the username or password were not filled
class LoginForm(FlaskForm):
    # Fill the fields
    # uuid = StringField("Uuid", default=uuid.uuid4, validators=[DataRequired(), UUID()])
    username = StringField("Username", validators=[DataRequired(), Length(max=50), Regexp(regex=r'^[A-Za-z]\w*$', message="This filed must start with a letter and constains only letters and numbers and underscores")])
    email = EmailField("Email", validators=[DataRequired(), Length(max=100)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Send")

class SignUpForm(FlaskForm):
    # Fill the fields
    username = StringField("Username", validators=[DataRequired(), Length(max=50), Regexp(regex=r'^[A-Za-z]\w*$', message="This filed must start with a letter and constains only letters and numbers and underscores")])
    email = EmailField("Email", validators=[DataRequired(), Length(max=100)])
    password = PasswordField("Password", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired(), Length(max=25), Regexp(regex=r'^\D*$', message="This field must contain only letters")])
    country = StringField("Country", validators=[DataRequired(), Length(max=35), Regexp(regex=r'^\D*$', message="This field must contain only letters")])
    submit = SubmitField("Send")

class ToDo(FlaskForm):
    description = StringField("Description", validators=[DataRequired(), Length(max=100)])
    submit = SubmitField("Create")

class Delete(FlaskForm):
    submit = SubmitField("Delete")

class Update(FlaskForm):
    submit = SubmitField("Update")
