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
	def select_user_money(user_id: int) -> int:
		user = User.query.filter(User.id == user_id).first()
		if user is None:
			return -1

		return user.money
	