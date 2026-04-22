from app.database import Select, Insert, Update

class BuyBusinessService:
	def __init__(self, business_id, user_id):
		self.business_id = business_id
		self.user_id = user_id

	# Get the data of the given business
	def get_business_data(self):
		business_data = Select.select_business(self.business_id)
		business_data["buyable"] = self.can_user_buy(business_data)
		
		return business_data
	
	# Check if the user has enough money to buy the business
	def can_user_buy(self, business_data: dict) -> bool:
		user_money = Select.select_user_money(self.user_id)
		if user_money >= business_data["price"]:
			return True
		
		return False
	
	# Use the user's money to buy the business
	def buy_business(self) -> str:
		business_data = self.get_business_data()
		user_money = Select.select_user_money(self.user_id)
		new_user_money = user_money - business_data["price"]

		if self.can_user_buy(business_data):
			Update.update_money(self.user_id, new_user_money)
			Insert.insert_owned_business(self.business_id, self.user_id)
		
		return "success"

	
	