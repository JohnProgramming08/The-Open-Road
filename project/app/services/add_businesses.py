from app.database import Insert
from app.database import Select
import json

class AddBusinessesService:
	def __init__(self):
		with open("app/services/businesses.json") as file:
			self.data = json.load(file)
	
	# Add all of the business types to the database
	def add_business_types(self) -> int:
		business_types = self.data["business_types"]
		for type in business_types:
			Insert.insert_business_type(type["type_name"], type["production_time"], type["stock_value"], type["supply_usage"], type["equipment_upgrade_price"], type["staff_upgrade_price"], type["security_upgrade_price"])
		
		return 67
	
	# Add all of the business locations to the database
	def add_business_locations(self) -> int:
		business_locations = self.data["business_locations"]
		for location in business_locations:
			Insert.insert_business_location(location)
		
		return 67
	
	# Add all of the businesses to the database
	def add_businesses(self) -> int:
		businesses = self.data["businesses"]
		for business in businesses:
			type_id = Select.select_business_type_id(business["type_name"])
			location_id = Select.select_business_location_id(business["location_name"])
			Insert.insert_business(business["price"], location_id, type_id, business["description"])

		return 67