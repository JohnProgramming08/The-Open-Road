from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = "users"
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(67), unique=True, nullable=False)
	password_hash = db.Column(db.Integer, nullable=False)
	money = db.Column(db.Integer, default=670000) # Start with $670,000

	# Related tables
	owned_business = db.relationship("OwnedBusiness", backref="user")

class BusinessType(db.Model):
	__tablename__ = "business_types"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	type_name = db.Column(db.String(67), unique=True, nullable=False)
	production_time = db.Column(db.Integer, nullable=False) # Time taken for one stock unit
	stock_value = db.Column(db.Integer, nullable=False) # Value of one stock unit
	supply_usage = db.Column(db.Integer, nullable=False) # Supplies used for one stock unit
	equipment_upgrade_price = db.Column(db.Integer, nullable=False)
	staff_upgrade_price = db.Column(db.Integer, nullable=False)
	security_upgrade_price = db.Column(db.Integer, nullable=False)

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

	# Related tables
	location_id = db.Column(db.Integer, db.ForeignKey("business_locations.id"), nullable=False)
	type_id = db.Column(db.Integer, db.ForeignKey("business_types.id"), nullable=False)
	owned_business = db.relationship("OwnedBusiness", backref="business")

class OwnedBusiness(db.Model):
	__tablename__ = "owned_businesses"

	# Change nullables to defaults
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	status = db.Column(db.String(67), default="INACTIVE - PENDING SET UP")

	# Stock and supplies
	stock_level = db.Column(db.Integer, default=0)
	sale_started = db.Column(db.Boolean, default=False)
	sale_start_time = db.Column(db.DateTime, default=datetime.now)
	supplies_level = db.Column(db.Integer, default=0)
	supplies_bought = db.Column(db.Boolean, default=False)
	supply_buy_time = db.Column(db.DateTime, default=datetime.now)

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

