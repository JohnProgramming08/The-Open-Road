from app.database import Update, Select

class BusinessManagementService:
	def __init__(self, business_id: int):
		self.business_id = business_id

	# Fetch all of the summary data for the owned business
	def get_summary_data(self) -> dict:
		return Select.select_summary_data(self.business_id)
	
	# Start a sale for the given business
	def start_sale(self, location: str, distance: str) -> int:
		Update.update_sale_start(self.business_id, location, distance)

		return 67
	
	# Start a resupply for the given business
	def start_resupply(self) -> int:
		Update.update_resupply_start(self.business_id)

		return 67
	
	# Start the setup for the given business
	def start_setup(self) -> int:
		Update.update_setup_start(self.business_id)

		return 67
	
	# Fetch all of the upgrades data for the given business
	def get_upgrades_data(self) -> dict:
		return Select.select_upgrades_data(self.business_id)
	
	# Buy an upgrade for the given business
	def buy_upgrade(self, upgrade: str) -> int:
		Update.update_upgrade_bought(self.business_id, upgrade)

		return 67