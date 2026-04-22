from flask import render_template, Blueprint, redirect, url_for
from app.services import BuyBusinessService
from app.forms import BuyBusinessForm

buy_business_bp = Blueprint("buy_business", __name__)

@buy_business_bp.route("/buy_business/<int:user_id>/<int:business_id>", methods=["GET", "POST"])
def buy_business(user_id: int, business_id: int):
	form = BuyBusinessForm()
	service = BuyBusinessService(business_id, user_id)
	business_data = service.get_business_data()

	# Get request
	if not form.validate_on_submit():
		return render_template("buy_business.html", id=user_id, business_id=business_id, business_data=business_data, bought=False, form=form)
	
	# Post request
	# Buy the business using the users money
	service.buy_business()

	return render_template("buy_business.html", id=user_id, business_data=business_data, bought=True, form=form)

