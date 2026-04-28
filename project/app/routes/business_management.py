
from flask import render_template, Blueprint, redirect, url_for
from app.services import BusinessManagementService
from app.forms import BusinessManagementForm

business_management_bp = Blueprint("business_management", __name__)

@business_management_bp.route("/business_management/<int:user_id>/<int:owned_business_id>", methods=["GET", "POST"])
def business_management(user_id: int, owned_business_id: int):
	form = BusinessManagementForm()
	
	# Get all of the data for the business
	service = BusinessManagementService(owned_business_id)
	summary_data = service.get_summary_data()
	upgrades_data = service.get_upgrades_data()
	
	# User has not submitted a form
	if not form.validate_on_submit():
		return render_template("business_management.html", id=user_id, summary_data=summary_data, upgrades_data=upgrades_data, button_clicked="")
	
	# User has submitted a form
	match form.button_clicked.data:
		case "setup":
			service.start_setup()
		
		case "resupply":
			service.start_resupply()

		case "sell":
			# Determine distance of sale
			location = form.location.data
			if location == "blaine_county" and summary_data["location"] == "Blaine County":
				distance = "close"
			elif location == "blaine_county":
				distance = "far"
			elif location == "los_santos" and summary_data["location"] == "Los Santos":
				distance = "close"
			elif location == "los_santos":
				distance = "far"

			service.start_sale(location, distance)

		case "security":
			service.buy_upgrade("security")
		
		case "staff":
			service.buy_upgrade("staff")

		case "equipment":
			service.buy_upgrade("equipment")

	return render_template("business_management.html", id=user_id, summary_data=summary_data, upgrades_data=upgrades_data, button_clicked=form.button_clicked)