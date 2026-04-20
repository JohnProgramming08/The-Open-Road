from app.database import Select

class HomeService:
	def __init__(self, user_id):
		self.user_id = user_id

	# Get all of the users owned businesses
	def get_owned_businesses(self):
		return Select.select_owned_businesses(self.user_id)
	
	# Get all of the businesses that the user does not own
	def get_unowned_businesses(self):
		businesses = Select.select_businesses()
		owned = Select.select_owned_businesses(self.user_id)
		result = []

		for business in businesses:
			unowned = True
			for owned_business in owned:
				if business["business_id"] == owned_business["business_id"]:
					unowned = False
					break # No point checking the rest
			
			if unowned:
				result.append(business)
		
		return result