from flask_wtf import FlaskForm
from wtforms import SubmitField

class BuyBusinessForm(FlaskForm):
	submit = SubmitField("Confirm")