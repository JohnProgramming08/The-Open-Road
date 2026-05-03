from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = "users"
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(67), unique=True, nullable=False)
	password_hash = db.Column(db.Integer, nullable=False)
	money = db.Column(db.Integer, default=670000) # Start with $670,000
	last_login_time = db.Column(db.Integer, default=int(datetime.now().timestamp()))

	# Related tables
	owned_business = db.relationship("OwnedBusiness", backref="user")

class BusinessType(db.Model):
	__tablename__ = "business_types"

	# Descriptions are redundant might delete them
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	type_name = db.Column(db.String(67), unique=True, nullable=False)
	production_time = db.Column(db.Integer, nullable=False) # Time taken for one stock unit
	stock_value = db.Column(db.Integer, nullable=False) # Value of one stock unit
	supply_usage = db.Column(db.Float, nullable=False) # Supplies used for one stock unit
	equipment_upgrade_price = db.Column(db.Integer, nullable=False)
	equipment_upgrade_description = db.Column(db.String(670), default="No description.")
	staff_upgrade_price = db.Column(db.Integer, nullable=False)
	staff_upgrade_description = db.Column(db.String(670), default="No description.")
	security_upgrade_price = db.Column(db.Integer, nullable=False)
	security_upgrade_description = db.Column(db.String(670), default="No description")

	# Related tables
	business = db.relationship("Business", backref="businesstype")

class BusinessLocation(db.Model):
	__tablename__ = "business_locations"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	location_name = db.Column(db.String(67), unique=True, nullable=False)

	# Related tables
	business = db.relationship("Business", backref="businesslocation")

class Business(db.Model):
	__tablename__ = "businesses"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)	
	price = db.Column(db.Integer, nullable=False) # Only add 2d.p. values
	description = db.Column(db.String(670), default="No description.")

	# Related tables
	location_id = db.Column(db.Integer, db.ForeignKey("business_locations.id"), nullable=False)
	type_id = db.Column(db.Integer, db.ForeignKey("business_types.id"), nullable=False)
	owned_business = db.relationship("OwnedBusiness", backref="business")

class OwnedBusiness(db.Model):
	__tablename__ = "owned_businesses"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	status = db.Column(db.String(67), default="INACTIVE - PENDING SET UP")

	# Stock and supplies
	stock_level = db.Column(db.Integer, default=0)
	sale_started = db.Column(db.Boolean, default=False)
	sale_finish_time = db.Column(db.Integer, default=int(datetime.now().timestamp()))
	sale_distance = db.Column(db.String(5), default="67") # close / far
	sale_location = db.Column(db.String(13), default="67") # Los Santos / Blaine County
	supplies_level = db.Column(db.Integer, default=0)
	supplies_bought = db.Column(db.Boolean, default=False)
	supply_arrive_time = db.Column(db.Integer, default=int(datetime.now().timestamp()))
	setup_finish_time = db.Column(db.Integer, default=int(datetime.now().timestamp()))
	setup_started = db.Column(db.Boolean, default=False)

	# Business stats
	total_earnings = db.Column(db.Integer, default=0)
	total_sales = db.Column(db.Integer, default=0)
	total_resupplies = db.Column(db.Integer, default=0)
	successful_resupplies = db.Column(db.Integer, default=0)
	total_los_santos_sales = db.Column(db.Integer, default=0)
	successful_los_santos_sales = db.Column(db.Integer, default=0)
	total_blaine_county_sales = db.Column(db.Integer, default=0)
	successful_blaine_county_sales = db.Column(db.Integer, default=0)
	production_ceased_supplies = db.Column(db.Integer, default=0)
	production_ceased_raided = db.Column(db.Integer, default=0)
	production_ceased_capacity = db.Column(db.Integer, default=0)

	# Upgrades
	equipment_upgrade_bought = db.Column(db.Boolean, default=False)
	staff_upgrade_bought = db.Column(db.Boolean, default=False)
	security_upgrade_bought = db.Column(db.Boolean, default=False)

	# Related tables
	business_id = db.Column(db.Integer, db.ForeignKey("businesses.id"), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

