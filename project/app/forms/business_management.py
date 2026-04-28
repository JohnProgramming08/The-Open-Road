from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired, Length

class BusinessManagementForm(FlaskForm):
	# Assigned automatically when a button is clicked, use js for this in front end
	button_clicked = RadioField(choices=[
		("setup", "Set Up"),
		("resupply", "Resupply"),
		("sell", "Sell Stock"),
		("security", "Security Upgrade"),
		("staff", "Staff Upgrade"),
		("equipment", "Equipment Upgrade")
	], validators=[DataRequired()])
	location = RadioField(choices=[
		("blaine_county", "Blaine County"),
		("los_santos", "Los Santos")
	])
	
	submit = SubmitField("Confirm")