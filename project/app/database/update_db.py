from .create_db import db, User

class Update:
	# Update the users money to a new given value
	@staticmethod
	def update_money(user_id: int, new_money: int) -> int:
		user = User.query.filter(User.id == user_id).first()
		user.money = new_money
		db.session.commit()
		
		return user.money 
