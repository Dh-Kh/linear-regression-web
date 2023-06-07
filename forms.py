from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    input_variable = IntegerField(validators=[DataRequired()])
    submit = SubmitField()