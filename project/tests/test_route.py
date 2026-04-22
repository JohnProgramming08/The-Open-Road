import pytest

# Index page
def test_index_get(one_hashed_user_client):
	response = one_hashed_user_client.get("/")
	assert response.status_code == 200
	assert b"Log In" in response.data

@pytest.mark.parametrize("username, password, log_in, sign_up", [
	("Dylan", "sigma", True, False),
	("dylan", "sigma", False, True),
	("dylan", "betas", False, True),
	("Jesus", "Christ", False, True)
])
def test_index_post_valid(one_hashed_user_client, username, password, log_in, sign_up):
	data = {
		"username": username,
		"password": password
	}
	if log_in:
		data["log_in"] = True
	if sign_up:
		data["sign_up"] = True

	response = one_hashed_user_client.post("/", data=data, follow_redirects=False)
	assert response.status_code == 200
	assert "/home/" in response.headers["Location"]

@pytest.mark.parametrize("username, password, log_in, sign_up, error", [
	("Dylan", "Sigma", False, True, b"username is taken"),
	("Dylan", "sigma", False, True, b"username is taken"),
	("Dylan", "nothing", False, True, b"username is taken"),
	("Dylan", "Sigma", True, False, b"details are incorrect"),
	("Thats", "FalseNews", True, False, b"details are incorrect")
])
def test_index_post_invalid(one_hashed_user_client, username, password, log_in, sign_up, error):
	data = {
		"username": username,
		"password": password
	}
	if log_in:
		data["log_in"] = True
	if sign_up:
		data["sign_up"] = True
	print(data)
	
	response = one_hashed_user_client.post("/", data=data, follow_redirects=True)
	assert response.status_code == 200
	assert error in response.data

# Home page
def test_home_get(one_owned_business_client):
	response = one_owned_business_client.get("/home/1")
	assert response.status_code == 200

# Buy business page
def test_business_page_get(one_business_user_client):
	response = one_business_user_client.get("/buy_business/1/1")
	assert response.status_code == 200

def test_business_page_post(one_business_user_client):
	data = {
		"submit": True
	}
	response = one_business_user_client.post("/buy_business/1/1", data=data)
	assert response.status_code == 200
