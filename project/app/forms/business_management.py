from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField
from wtforms.validators import DataRequired, Length

class BusinessManagementForm(FlaskForm):
	# Assigned automatically when a button is clicked, use js for this in front end
	# setup, resupply, sell, security, staff, equipment
	button_clicked = StringField(validators=[DataRequired()], render_kw={"class": "hidden", "id": "button-clicked"})
	# blaine_county, los_santos
	location = StringField(render_kw={"class": "hidden", "id": "location"})
	# close, far
	distance = StringField(render_kw={"class": "hidden", "id": "distance"})
	
	submit = SubmitField("Confirm")