from app.database import Update
import pytest
from datetime import datetime

# Changing user's money
@pytest.mark.parametrize("new_money", [
	69, 0, 643563463
])
def test_update_money(one_user_app, new_money):
	with one_user_app.app_context():
		assert Update.update_money(1, new_money) == new_money

# Changing users last login time
def test_update_last_login_time(one_user_app):
	with one_user_app.app_context():
		time = int(datetime.now().timestamp())
		assert Update.update_last_login_time(1, time) == time

# Changing owned businesses time based data
def test_update_business_time_data(one_owned_business_app):
	data = {
		"total_earnings": 4132,
		"stock_level": 100,
		"total_sales": 4, 
		"total_los_santos_sales": 3,
		"successful_los_santos_sales": 0,
		"total_blaine_county_sales": 1,
		"successful_blaine_county_sales": 1,
		"sale_started": False,
		"total_resupplies": 4,
		"successful_resupplies": 4,
		"supplies_level": 67,
		"supplies_bought": True,
		"setup_started": False,
		"status": "ACTIVE"
	}

	with one_owned_business_app.app_context():
		assert Update.update_business_time_data(1, data) == 67
