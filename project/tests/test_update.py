from app.database import Update
import pytest

# Changing user's money
@pytest.mark.parametrize("new_money", [
	69, 0, 643563463
])
def test_update_money(one_user_app, new_money):
	with one_user_app.app_context():
		assert Update.update_money(1, new_money) == new_money