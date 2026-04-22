from app.database import Select
import pytest

# Fetching a user ID
@pytest.mark.parametrize("username, password_hash, id", [
	("Dylan", 67, 1),
	("Dylan", 68, -1),
	("dylan", 67, -1),
	("josh", 69, -1)
])
def test_select_user(one_user_app, username, password_hash, id):
	with one_user_app.app_context():
		assert Select.select_user_id(username, password_hash) == id

# Checking if a username exists
@pytest.mark.parametrize("username, result", [
	("Dylan", True),
	("dylan", False),
	("Josh", False)
])
def test_username_exists(one_user_app, username, result):
	with one_user_app.app_context():
		assert Select.username_exists(username) == result

# Fetching owned business data
def test_select_owned_businesses_valid(one_owned_business_app):
	data = []
	with one_owned_business_app.app_context():
		data = Select.select_owned_businesses(1)

	assert len(data) == 1
	data = data[0]
	assert data["type"] == "Weed"
	assert data["location"] == "Paleto Bay"
	assert data["price"] == 67

def test_select_owned_business_invalid(one_owned_business_app):
	with one_owned_business_app.app_context():
		data = Select.select_owned_businesses(67)
		assert len(data) == 0

# Fetching business data
def test_select_businesses(one_owned_business_app):
	with one_owned_business_app.app_context():
		data = Select.select_businesses()
		
	assert len(data) == 1
	data = data[0]
	assert data["business_id"] == 1
	assert data["type"] == "Weed"
	assert data["location"] == "Paleto Bay"
	assert data["price"] == 67

def test_select_business_valid(one_owned_business_app):
	with one_owned_business_app.app_context():
		data = Select.select_business(1)
		
		assert data["id"] == 1
		assert data["location"] == "Paleto Bay"
		assert data["type"] == "Weed"
		assert data["price"] == 67
		assert data["description"] == "No description."

def test_select_business_invalid(one_owned_business_app):
	with one_owned_business_app.app_context():
		assert Select.select_business(67) == {}

# Fetching a users money
def test_select_user_money_valid(one_user_app):
	with one_user_app.app_context():
		assert Select.select_user_money(1) == 670000

def test_select_user_movey_invalid(one_user_app):
	with one_user_app.app_context():
		assert Select.select_user_money(67) == -1
