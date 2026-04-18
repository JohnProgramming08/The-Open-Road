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
