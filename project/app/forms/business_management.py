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
	], validators=[DataRequired()], render_kw={"class": "hidden", "id": "button-clicked"})
	location = RadioField(choices=[
		("blaine_county", "Blaine County"),
		("los_santos", "Los Santos")
	], render_kw={"class": "hidden", "id": "location"})
	distance = RadioField(choices=[
		("close", "Close"),
		("far", "Far")
	], render_kw={"class": "hidden", "id": "distance"})
	
	submit = SubmitField("Confirm")