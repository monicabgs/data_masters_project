from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, FloatField,validators
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")

class DataForm(Form):
    input_data = StringField("input_data", validators=[DataRequired()])

class ResultForm(Form):
    model_result = StringField("model_result", validators=[DataRequired()])