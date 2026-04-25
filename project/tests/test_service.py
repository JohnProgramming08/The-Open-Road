from app.services import IntroService, HomeService, BuyBusinessService, TimeService
import pytest

# Intro service
@pytest.mark.parametrize("username, password, id", [
	("Dylan", "sigma", 1),
	("Lewis", "Beta", -1),
	("67", "69", -1)
])
def test_get_user_id(one_hashed_user_app, username, password, id):
	with one_hashed_user_app.app_context():
		service = IntroService(username, password)
		assert service.get_user_id() == id

@pytest.mark.parametrize("username, password, id", [
	("Dylan", "Alpha", -1),
	("Dylan", "sigma", -1),
	("dylan", "beta", 2),
	("that", "guy", 2)
])
def test_add_user(one_hashed_user_app, username, password, id):
	with one_hashed_user_app.app_context():
		service = IntroService(username, password)
		assert service.add_user() == id

# Home service
def test_get_owned_businesses(one_owned_business_app):
	with one_owned_business_app.app_context():
		service = HomeService(1)
		assert len(service.get_owned_businesses()) == 1

def test_get_unowned_businesses_none(one_owned_business_app):
	with one_owned_business_app.app_context():
		service = HomeService(1)
		assert len(service.get_unowned_businesses()) == 0

def test_get_unowned_businesses_one(one_business_user_app):
	with one_business_user_app.app_context():
		service = HomeService(1)
		assert len(service.get_unowned_businesses()) == 1

# Buy business service
# User has 670,000
@pytest.mark.parametrize("price, buyable", [
	(420000, True),
	(670000, True),
	(670001, False),
	(67, True),
	(6454234, False)
])
def test_can_user_buy(one_business_user_app, price, buyable):
	with one_business_user_app.app_context():
		service = BuyBusinessService(1, 1)
		assert service.can_user_buy({"price": price}) == buyable

def test_get_business_data(one_business_user_app):
	with one_business_user_app.app_context():
		service = BuyBusinessService(1, 1)
		data = service.get_business_data()
		assert data["id"] == 1
		assert data["location"] == "Paleto Bay"
		assert data["type"] == "Weed"
		assert data["price"] == 67
		assert data["buyable"] == True
		assert data["description"] == "No description."

def test_buy_business(one_business_user_app):
	with one_business_user_app.app_context():
		service = BuyBusinessService(1, 1)
		assert service.buy_business() == "success"

# Time service
def test_get_owned_business_data(one_owned_business_app):
	with one_owned_business_app.app_context():
		service = TimeService(1)
		assert len(service.get_owned_business_data()) == 1

def test_make_sale(one_owned_business_app):
	data = {
		"stock_level": 69,
		"sale_distance": "far",
		"total_earnings": 670,
		"total_sales": 2,
		"sale_destination": "Los Santos",
		"total_los_santos_sales": 2,
		"successful_los_santos_sales": 2,
		"total_blaine_county_sales": 0,
		"successful_blaine_county_sales": 0,
		"stock_value": 67,
		"sale_started": True
	}
	with one_owned_business_app.app_context():
		service = TimeService(1)
		assert service.make_sale(data) == 67

def test_resupply(one_owned_business_app):
	data = {
		"supplies_level": 0,
		"supplies_bought": True,
		"total_resupplies": 2,
		"successful_resupplies": 2
	}
	with one_owned_business_app.app_context():
		service = TimeService(1)
		assert service.resupply(data) == 67

def test_make_product(one_owned_business_app):
	data = {
		"stock_level": 1,
		"supply_level": 12,
		"supply_usage": 4
	}
	with one_owned_business_app.app_context():
		service = TimeService(1)
		assert service.make_product(data) == 67

def test_setup_business(one_owned_business_app):
	data = {
		"status": "INACTIVE - NEEDS SETTING UP",
		"supplies_level": 0,
		"setup_started": True
	}
	with one_owned_business_app.app_context():
		service = TimeService(1)
		assert service.setup_business(data) == 67

def test_update_owned_business_data(one_owned_business_app):
	with one_owned_business_app.app_context():
		service = TimeService(1)
		assert service.update_owned_business_data() == False