from app.database import Insert
from sqlalchemy.exc import IntegrityError
import pytest

# Adding a new user
# Data: username, password_hash
@pytest.mark.parametrize("username, password_hash", [
	("Dylan", 67),
	("Dylan", -67),
	("joshy", 0),
	("12", 762348952)
])
def test_insert_user_valid(app, username, password_hash):
	with app.app_context():
		assert Insert.insert_user(username, password_hash) == 1

def test_insert_user_invalid(app):
	with app.app_context():
		Insert.insert_user("Dylan", 12)
		with pytest.raises(IntegrityError):
			Insert.insert_user("Dylan", 12)

# Adding a new business type
@pytest.mark.parametrize("name, production_time, stock_value, supply_usage, equipment_price, staff_price, security_price", [
	("Weed", 5, 100, 50, 100000, 200000, 300000),
	("Dope", 10, 1000, 33, 350000, 200000, 670000),
	("Dylan Scully", 9, 67, 67, 67, 67, 67)
])
def test_insert_business_type_valid(app, name, production_time, stock_value, supply_usage, equipment_price, staff_price, security_price):
	with app.app_context():
		assert Insert.insert_business_type(name, production_time, stock_value, supply_usage, equipment_price, staff_price, security_price) == 1

def test_insert_business_type_invalid(app):
	with app.app_context():
		Insert.insert_business_type("Dylan Scully", 9, 67, 67, 67, 67, 67)
		with pytest.raises(IntegrityError):
			Insert.insert_business_type("Dylan Scully", 69, 69, 69, 69, 69, 69)

# Adding a new business location
@pytest.mark.parametrize("location", [
	"Wythenshawe",
	"Parrs Wood Sixth Form",
	"Paleto Bay",
	"SG7"
])
def test_insert_business_location_valid(app, location):
	with app.app_context():
		assert Insert.insert_business_location(location) == 1

def test_insert_business_location_invalid(app):
	with app.app_context():
		Insert.insert_business_location("Dylan's House")
		with pytest.raises(IntegrityError):
			Insert.insert_business_location("Dylan's House")

# Adding a new business
@pytest.mark.parametrize("price", [
	500000,
	850000,
	67,
	1250000
])
def test_insert_business(business_location_type_app, price):
	with business_location_type_app.app_context():
		assert Insert.insert_business(price, 1, 1) == 1

# Adding a new owned business
def test_insert_owned_business(one_business_user_app):
	with one_business_user_app.app_context():
		assert Insert.insert_owned_business(1, 1) == 1