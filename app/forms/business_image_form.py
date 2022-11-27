from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, BooleanField, IntegerField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Email, ValidationError, Length, NumberRange, Regexp
from app.models import BusinessImage



class BusinessImageForm(FlaskForm):
    url = StringField("url", validators=[DataRequired()])
    preview = BooleanField("preview", validators=[DataRequired(), Length(min=1, max=255, message='URL must be between 1 and 255 characters.')])
    submit = SubmitField("submit")
