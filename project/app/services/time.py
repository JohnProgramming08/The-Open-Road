from app.database import Update, Select
from datetime import datetime
import random


class TimeService:
	def __init__(self, user_id: int):
		self.user_id = user_id
		self.business_data = self.get_owned_business_data()

	# Tested
	# Get all of the users owned business data
	def get_owned_business_data(self) -> list:
		businesses = Select.select_owned_businesses(self.user_id)
		res = []
		for business in businesses:
			res.append(Select.select_owned_business_time_data(business["owned_business_id"]))

		return res	
	
	# Add sale money to users account and reset stock
	def make_sale(self, business: dict) -> int:
		money_made = business["stock_level"] * business["stock_value"]
		if business["sale_distance"] == "far":
			money_made *= 1.5

		user_money = Select.select_user_money(self.user_id)
		Update.update_money(self.user_id, money_made + user_money)

		# Update business data
		business["stock_level"] = 0
		business["sale_started"] = False
		business["total_earnings"] += money_made
		business["total_sales"] += 1
		if business["sale_location"] == "Los Santos":
			business["total_los_santos_sales"] += 1
			business["successful_los_santos_sales"] += 1
		else:
			business["total_blaine_county_sales"] += 1
			business["successful_blaine_county_sales"] += 1

		return 67

	# Fill up the businesses supplies
	def resupply(self, business: dict) -> int:
		business["supplies_level"] = 100
		business["supplies_bought"] = False
		business["total_resupplies"] += 1
		business["successful_resupplies"] += 1

		return 67
	
	# Produce a unit of product
	def make_product(self, business: dict) -> int:
		business["stock_level"] += 1
		business["supplies_level"] -= business["supply_usage"]

		return 67
	
	# Setup the business
	def setup_business(self, business: dict) -> bool:
		business["status"] = "ACTIVE"
		business["supplies_level"] = 100
		business["setup_started"] = True

		return 67
	
	# Raid the business
	def raid_business(self, business: dict):
		business["stock_level"] = 0
		business["supplies_level"] = 0
		business["status"] = "INACTIVE - PENDING SET UP"
		business["production_ceased_raided"] += 1
		business["setup_started"] = False

	# Sale has failed
	def sale_failed(self, business: dict):
		business["stock_level"] = int(0.8 * business["stock_level"])
		business["sale_started"] = False
		business["total_sales"] += 1
		if business["sale_location"] == "Los Santos":
			business["total_los_santos_sales"] += 1
		else:
			business["total_blaine_county_sales"] += 1

	# Resupply has failed
	def resupply_failed(self, business: dict):
		business["supplies_bought"] = False
		business["total_resupplies"] += 1 

	# Update all of the users owned business data based on time since last login
	def update_owned_business_data(self):
		change_made = False
		last_login_time = Select.select_last_login_time(self.user_id)
		current_time = int(datetime.now().timestamp())
		# Time difference in seconds
		time_difference = current_time - last_login_time

		for business in self.business_data:
			business_time_difference = time_difference
			raid = random.randint(1, 20) == 20 and not business["security_upgrade_bought"]
			resupply_fail = random.randint(1, 20) == 20 and not business["security_upgrade_bought"]
			sale_fail = random.randint(1, 20) == 20 and not business["security_upgrade_bought"]

			# Check for upgrades
			if business["staff_upgrade_bought"]:
				business_time_difference *= 1.25
				business["stock_value"] *= 1.5
			if business["equipment_upgrade_bought"]:
				business_time_difference *= 1.5
				business["stock_value"] *= 2
				business["supply_usage"] = round(0.75 * business["supply_usage"])

			# Sale made
			if current_time >= business["sale_finish_time"] and business["sale_started"] and not sale_fail and business["status"] != "INACTIVE - PENDING SET UP":
				change_made = True
				business["status"] = "ACTIVE"
				self.make_sale(business)
			elif current_time >= business["sale_finish_time"] and business["sale_started"]:
				change_made = True
				business["status"] = "ACTIVE"
				self.sale_failed(business)

			# Product being made before supplies arrived
			while time_difference >= business["production_time"] and business["supplies_level"] >= business["supply_usage"] and business["stock_level"] < 100:
				change_made = True
				time_difference -= business["production_time"]
				self.make_product(business)

			# Production stopped
			production_stopped = False
			if business["supplies_level"] < business["supply_usage"] and business["status"] == "ACTIVE":
				business["production_ceased_supplies"] += 1
				production_stopped = True
				change_made = True
			if business["stock_level"] == 100 and business["status"] == "ACTIVE":
				business["production_ceased_capacity"] += 1
				production_stopped = True
				change_made = True
			if production_stopped:
				business["status"] = "SUSPENDED"

			# Supplies arrived
			if current_time >= business["supply_arrive_time"] and business["supplies_bought"] and not resupply_fail and business["status"] != "INACTIVE - PENDING SET UP":
				change_made = True
				business["status"] = "ACTIVE"
				self.resupply(business)
			elif current_time >= business["supply_arrive_time"] and business["supplies_bought"]:
				change_made = True
				business["status"] = "ACTIVE"
				self.resupply_failed(business)

			# Business has been setup
			if current_time >= business["setup_finish_time"] and business["setup_started"] and business["status"] == "INACTIVE - PENDING SET UP":
				change_made = True
				time_difference -= 600
				self.setup_business(business)

			# Product being made after supplies arrived
			while time_difference >= business["production_time"] and business["supplies_level"] >= business["supply_usage"] and business["stock_level"] < 100:
				change_made = True
				time_difference -= business["production_time"]
				self.make_product(business)

			# Businesss was raided
			if time_difference > 7200 and raid:
				change_made = True
				self.raid_business(business)

			# Only update the database if a change was made
			if change_made:
				Update.update_last_login_time(self.user_id, current_time)
				Update.update_business_time_data(business["id"], business)

		return change_made

# Maybe add a time service that can be called on a timeout when sale started or smth to auto update page
