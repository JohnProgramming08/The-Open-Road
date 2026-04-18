from .create_db import User, db

class Insert:
	# Add a new user to the database and return their id
	@staticmethod
	def insert_user(username: str, password_hash: int) -> int:
		new_user = User(username=username, password_hash=password_hash)
		db.session.add(new_user)
		db.session.commit()

		return new_user.id