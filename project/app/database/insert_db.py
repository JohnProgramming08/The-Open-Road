from .create_db import User, OwnedBusiness, Business, BusinessType, BusinessLocation, db

class Insert:
	# Add a new user to the database and return their id
	@staticmethod
	def insert_user(username: str, password_hash: int) -> int:
		new_user = User(username=username, password_hash=password_hash)
		db.session.add(new_user)
		db.session.commit()

		return new_user.id
	
	# Add a new business type to the database
	@staticmethod
	def insert_business_type(name: str, production_time: int, stock_value: int, supply_usage: int, equipment_price: int, staff_price: int, security_price: int) -> int:
		new_business_type = BusinessType(type_name=name, production_time=production_time, stock_value=stock_value, supply_usage=supply_usage, equipment_upgrade_price=equipment_price, staff_upgrade_price=staff_price, security_upgrade_price=security_price)
		db.session.add(new_business_type)
		db.session.commit()

		return new_business_type.id

	# Add a new business location to the database
	@staticmethod
	def insert_business_location(name: str) -> int:
		new_business_location = BusinessLocation(location_name=name)
		db.session.add(new_business_location)
		db.session.commit()

		return new_business_location.id
	
	# Add a new business to the database
	@staticmethod
	def insert_business(price: int, location_id: int, type_id: int, description: str = None) -> int:
		if description is None:
			new_business = Business(price=price, location_id=location_id, type_id=type_id)
		else:
			new_business = Business(price=price, location_id=location_id, type_id=type_id, description=description)
		db.session.add(new_business)
		db.session.commit()

		return new_business.id

	# Add a new owned business to the database
	@staticmethod
	def insert_owned_business(business_id, user_id):
		new_owned_business = OwnedBusiness(business_id=business_id, user_id=user_id)
		db.session.add(new_owned_business)
		db.session.commit()

		return new_owned_business.id
	