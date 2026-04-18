from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length

class IntroForm(FlaskForm):
	username = StringField("User:", validators=[DataRequired(), Length(min=5, max=67)])
	password = PasswordField("Password", validators=[DataRequired(), Length(min=5, max=67)])
	log_in = SubmitField("Log In")
	sign_up = SubmitField("Sign Up")