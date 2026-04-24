from .create_db import db, User, OwnedBusiness

class Update:
	# Update the users money to a new given value
	@staticmethod
	def update_money(user_id: int, new_money: int) -> int:
		user = User.query.filter(User.id == user_id).first()
		user.money = new_money
		db.session.commit()
		
		return user.money 
	
	# Upate the users last login time
	@staticmethod
	def update_last_login_time(id: int, new_time: int) -> int:
		user = User.query.filter(User.id == id).first()
		user.last_login_time = new_time
		db.session.commit()

		return user.last_login_time
	
	# Update the time based data of a given business
	@staticmethod
	def update_business_time_data(id: int, updated_data: dict) -> int:
		business = OwnedBusiness.query.filter(OwnedBusiness.id == id).first()
		business.stock_level = updated_data["stock_level"]
		business.sale_started = updated_data["sale_started"]
		business.supplies_level = updated_data["supplies_level"]
		business.supplies_bought = updated_data["supplies_bought"]
		business.setup_started = updated_data["setup_started"]
		business.status = updated_data["status"]
		db.session.commit()

		return 67