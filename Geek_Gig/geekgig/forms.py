from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from geekgig.models import Admin, Supplier
from flask_login import current_user

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class DataForm(FlaskForm):
    beds = StringField('Number of beds required', validators=[DataRequired()])
    oxygen = StringField('Number of oxygen cylinders required', validators=[DataRequired()])
    icu = StringField('Number of icu required', validators=[DataRequired()])
    month_posted = StringField('Month Posted', validators=[DataRequired()])
    submit = SubmitField('Post')