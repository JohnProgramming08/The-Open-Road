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