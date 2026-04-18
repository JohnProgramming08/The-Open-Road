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