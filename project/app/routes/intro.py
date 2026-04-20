from flask import render_template, Blueprint, redirect, url_for
from app.services import IntroService
from app.forms import IntroForm


intro_bp = Blueprint("intro", __name__)

@intro_bp.route("/", methods=["GET", "POST"])
def intro():
	form = IntroForm()
	# Get request
	if not form.validate_on_submit():
		return render_template("index.html", form=form, error="")
	
	# Post request
	username = form.username.data
	password = form.password.data
	service = IntroService(username, password)

	# User is attempting to log in 
	if form.log_in.data:
		print("logging in")
		user_id = service.get_user_id()
		if user_id == -1:
			return render_template("index.html", form=form, error="Your login details are incorrect.")
		
		return redirect(url_for("home.home", id=user_id)), 200
	
	# User is attempting to sign up
	elif form.sign_up.data:
		user_id = service.add_user()
		if user_id == -1:
			return render_template("index.html", form=form, error="That username is taken.")
		
		return redirect(url_for("home.home", id=user_id)), 200