import pytest
import hashlib
from app import create_app
from app.database import Insert


@pytest.fixture
def app():
	app = create_app({
		"TESTING": True,
		"WTF_CSRF_ENABLED": False, # <--- Disable CSRF for easier testing
		"SECRET_KEY": "test-secret",
		"SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
	})
	yield app

@pytest.fixture
def client(app):
	return app.test_client()

# App with one user
@pytest.fixture
def one_user_app(app):
	with app.app_context():
		Insert.insert_user("Dylan", 67)
    
	return app

# App with one user with hashed password
@pytest.fixture
def one_hashed_user_app(app):
	with app.app_context():
		full_hashed_password = int(
            hashlib.sha256("sigma".encode("utf-8")).hexdigest(), 16
        )
		password_hash = full_hashed_password % (10**8)
		Insert.insert_user("Dylan", password_hash)
		
	return app

# Test client, one user with hashed password
@pytest.fixture
def one_hashed_user_client(one_hashed_user_app):
	return one_hashed_user_app.test_client()

# App with a business location and type
@pytest.fixture
def business_location_type_app(app):
	with app.app_context():
		Insert.insert_business_location("Paleto Bay")
		Insert.insert_business_type("Weed", 5, 100, 1, 100000, 125000, 200000)

	return app	

# App with a business and a user
@pytest.fixture
def one_business_user_app(business_location_type_app):
	with business_location_type_app.app_context():
		Insert.insert_business(67, 1, 1)
		Insert.insert_user("Dylan", "Sigma")

	return business_location_type_app

# App with an owned business
@pytest.fixture
def one_owned_business_app(one_business_user_app):
	with one_business_user_app.app_context():
		Insert.insert_owned_business(1, 1)
	
	return one_business_user_app

# Test client with an owned business
@pytest.fixture
def one_owned_business_client(one_owned_business_app):
	return one_owned_business_app.test_client()