from app.database import Insert, Select
import hashlib

class IntroService:
	def __init__(self, username: str, password: str) -> None:
		self.username = username
		self.password_hash = self.hash(password)
	
	# Return the hash of the given string
	def hash(self, password: str) -> int:
		full_hashed_password = int(
            hashlib.sha256(password.encode("utf-8")).hexdigest(), 16
        )
		password_hash = full_hashed_password % (10**8)
		
		return password_hash
	
	# Return the id of the user with the given details (-1 if None)
	def get_user_id(self) -> int:
		return Select.select_user_id(self.username, self.password_hash)
	
	# Add a new user to the database, returning their id (-1 if failed)
	def add_user(self) -> int:
		if Select.username_exists(self.username): # Unique usernames
			return -1
		
		return Insert.insert_user(self.username, self.password_hash)
	
