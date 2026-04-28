from .create_db import db, User, OwnedBusiness
from datetime import datetime

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
		business.total_earnings = updated_data["total_earnings"]
		business.stock_level = updated_data["stock_level"]
		
		business.total_sales = updated_data["total_sales"]
		business.total_los_santos_sales = updated_data["total_los_santos_sales"]
		business.successful_los_santos_sales = updated_data["successful_los_santos_sales"]
		business.total_blaine_county_sales = updated_data["total_blaine_county_sales"]
		business.successful_blaine_county_sales = updated_data["successful_blaine_county_sales"]
		business.sale_started = updated_data["sale_started"]
		
		business.total_resupplies = updated_data["total_resupplies"]
		business.successful_resupplies = updated_data["successful_resupplies"]
		business.supplies_level = updated_data["supplies_level"]
		business.supplies_bought = updated_data["supplies_bought"]
		
		business.setup_started = updated_data["setup_started"]
		business.status = updated_data["status"]
		db.session.commit()

		return 67
	
	# Update the sale start data of an owned business
	@staticmethod
	def update_sale_start(id: int, location: str, distance: str) -> int:
		business = OwnedBusiness.query.filter(OwnedBusiness.id == id).first()
		business.sale_started = True
		business.sale_finish_time = datetime.now().timestamp() + 1500
		business.sale_location = location
		business.sale_distance = distance
		db.session.commit()

		return 67
	
	# Update the setup start date of an owned business
	@staticmethod
	def update_setup_start(id: int):
		business = OwnedBusiness.query.filter(OwnedBusiness.id == id).first()
		business.setup_started = True
		business.setup_finish_time = datetime.now().timestamp() + 900
		db.session.commit()

		return 67
	
	# Update the resupply start data of an owned business
	@staticmethod
	def update_resupply_start(id: int):
		business = OwnedBusiness.query.filter(OwnedBusiness.id == id).first()
		business.supplies_bought = True
		business.supply_arrive_time = datetime.now().timestamp() + 1200
		db.session.commit()

		return 67
	
	# Update the bought status of an upgrade
	def update_upgrade_bought(id: int, upgrade: str) -> int:
		business = OwnedBusiness.query.filter(OwnedBusiness.id == id).first()

		if upgrade == "staff":
			business.staff_upgrade_bought = True
		elif upgrade == "equipment":
			business.equipment_upgrade_bought = True
		elif upgrade == "security":
			business.security_upgrade_bought = True
		db.session.commit()

		return 67