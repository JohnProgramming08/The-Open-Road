from flask import render_template, Blueprint, redirect, url_for
from app.services import HomeService, TimeService

home_bp = Blueprint("home", __name__)

@home_bp.route("/home/<int:id>")
def home(id: int):
	time_service = TimeService(id)
	time_service.update_owned_business_data()

	# Get all businesses filtered by owned and unowned
	service = HomeService(id)
	owned_businesses = service.get_owned_businesses()
	unowned_businesses = service.get_unowned_businesses()

	return render_template("home.html", id=id, owned_businesses=owned_businesses, unowned_businesses=unowned_businesses)