from .create_db import db, User

class Select:
	# Get the id of the user with the given username and password hash
	@staticmethod
	def select_user_id(username: str, password_hash: int) -> int:
		user = User.query.filter((User.username == username) & (User.password_hash == password_hash)).first()
		if user is None:
			return -1
		
		return user.id
	
	# Return whether or not a given username is used in the database
	@staticmethod
	def username_exists(username: str) -> bool:
		users = User.query.filter(User.username == username).all()
		if len(users) == 0:
			return False
		
		return True