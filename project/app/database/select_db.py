from .create_db import db, User, OwnedBusiness, Business, BusinessType, BusinessLocation

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
	
	# Return data about every business the user owns
	@staticmethod
	def select_owned_businesses(user_id: int) -> list[dict]:
		owned_businesses = OwnedBusiness.query.filter(OwnedBusiness.user_id == user_id).all()
		res = []
		for owned_business in owned_businesses:
			business_type = owned_business.business.businesstype.type_name
			business_location = owned_business.business.businesslocation.location_name
			business_price = owned_business.business.price
			business_id = owned_business.business.id
			stock_level = owned_business.stock_level
			supplies_level = owned_business.supplies_level

			res.append({
				"business_id": business_id,
				"type": business_type,
				"location": business_location,
				"price": business_price,
				"stock": stock_level,
				"supplies": supplies_level
			})

		return res
	
	# Get all business data
	@staticmethod
	def select_businesses() -> list[dict]:
		businesses = Business.query.all()
		res = []
		for business in businesses:
			business_type = business.businesstype.type_name
			business_location = business.businesslocation.location_name

			res.append({
				"business_id": business.id,
				"type": business_type,
				"location": business_location,
				"price": business.price
			})
		
		return res
	
	# Get buying data for a specific businiess
	@staticmethod
	def select_business(business_id: int) -> dict:
		business = Business.query.filter(Business.id == business_id).first()
		if business is None:
			return {}

		res = {}
		res["id"] = business_id
		res["location"] = business.businesslocation.location_name
		res["type"] = business.businesstype.type_name
		res["price"] = business.price
		res["description"] = business.description

		return res
	
	# Get how much money the user has
	@staticmethod
	def select_user_money(user_id: int) -> int:
		user = User.query.filter(User.id == user_id).first()
		if user is None:
			return -1

		return user.money
	
	# Get all of the data of an owned business related to time passed
	@staticmethod
	def select_owned_business_time_data(id: int) -> dict:
		owned_business = OwnedBusiness.query.filter(id == OwnedBusiness.id).first()
		if owned_business is None:
			return {}

		res = {}
		res["id"] = owned_business.id
		res["total_earnings"] = owned_business.total_earnings
		res["stock_level"] = owned_business.stock_level
		res["stock_value"] = owned_business.business.businesstype.stock_value
		
		res["total_sales"] = owned_business.total_sales
		res["total_los_santos_sales"] = owned_business.total_los_santos_sales
		res["successful_los_santos_sales"] = owned_business.successful_los_santos_sales
		res["total_blaine_county_sales"] = owned_business.total_blaine_county_sales
		res["successful_blaine_county_sales"] = owned_business.successful_blaine_county_sales
		res["sale_started"] = owned_business.sale_started
		res["sale_finish_time"] = owned_business.sale_finish_time
		res["sale_distance"] = owned_business.sale_distance
		res["sale_location"] = owned_business.sale_location
		
		res["total_resupplies"] = owned_business.total_resupplies
		res["successful_resupplies"] = owned_business.successful_resupplies
		res["supplies_level"] = owned_business.supplies_level
		res["supplies_bought"] = owned_business.supplies_bought
		res["supply_arrive_time"] = owned_business.supply_arrive_time
		
		res["setup_finish_time"] = owned_business.setup_finish_time
		res["setup_started"] = owned_business.setup_started
		res["production_time"] = owned_business.business.businesstype.production_time
		res["supply_usage"] = owned_business.business.businesstype.supply_usage
		res["status"] = owned_business.status

		return res 
	
	# Get the last time the user logged in
	@staticmethod
	def select_last_login_time(id: int) -> int:
		user = User.query.filter(User.id == id).first()
		
		return user.last_login_time

	# Get the summary data for an owned business
	@staticmethod
	def select_summary_data(id: int) -> dict:
		business = OwnedBusiness.query.filter(OwnedBusiness.id == id).first()
		if business.total_resupplies != 0:
			resupply_success_rate = int((business.successful_resupplies / business.total_resupplies) * 100)
		else:
			resupply_success_rate = 0
		
		if business.total_los_santos_sales != 0:
			sell_success_rate_los_santos = int((business.successful_los_santos_sales / business.total_los_santos_sales) * 100)
		else:
			sell_success_rate_los_santos = 0
		
		if business.total_blaine_county_sales != 0:
			sell_success_rate_blaine_county = int((business.successful_blaine_county_sales / business.total_blaine_county_sales) * 100)
		else:
			sell_success_rate_blaine_county = 0

		res = {
			"location": business.business.businesslocation.location_name,
			"type": business.business.businesstype.type_name,
			"status": business.status,
			"stock_level": business.stock_level,
			"supplies_level": business.supplies_level,
			"total_earnings": business.total_earnings,
			"total_sales": business.total_sales,
			"resupply_success_rate": resupply_success_rate,
			"sell_success_rate_los_santos": sell_success_rate_los_santos,
			"sell_success_rate_blaine_county": sell_success_rate_blaine_county,
			"production_ceased_supplies": business.production_ceased_supplies,
			"production_ceased_raided": business.production_ceased_raided,
			"production_ceased_capacity": business.production_ceased_capacity
		}

		return res
	
	# Get the upgrades data for an owned business
	def select_upgrades_data(id: int) -> dict:
		business = OwnedBusiness.query.filter(OwnedBusiness.id == id).first()
		staff_description = business.business.businesstype.staff_upgrade_description
		staff_price = business.business.businesstype.staff_upgrade_price
		security_description = business.business.businesstype.security_upgrade_description
		security_price = business.business.businesstype.security_upgrade_price
		equipment_description = business.business.businesstype.equipment_upgrade_description
		equipment_price = business.business.businesstype.equipment_upgrade_price

		return {
			"staff_description": staff_description,
			"staff_price": staff_price,
			"staff_bought": business.staff_upgrade_bought,
			"security_description": security_description,
			"security_price": security_price,
			"security-bought": business.security_upgrade_bought,
			"equipment_description": equipment_description,
			"equipment_price": equipment_price,
			"equipment_bought": business.equipment_upgrade_bought
		}
	
	# Both still need testing
	# Get the id of a given business location
	def select_business_location_id(location_name: str) -> int:
		location = BusinessLocation.query.filter(location_name == BusinessLocation.location_name).first()
		return location.id
	
	# Get the id of a given business_type
	def select_business_type_id(type_name: str) -> int:
		type = BusinessType.query.filter(type_name == BusinessType.type_name).first()
		return type.id