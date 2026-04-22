from app.services import IntroService, HomeService, BuyBusinessService
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