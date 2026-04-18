from app.services import IntroService
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
