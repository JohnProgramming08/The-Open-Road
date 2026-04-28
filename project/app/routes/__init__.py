from .intro import intro_bp
from .home import home_bp
from .buy_business import buy_business_bp
from .business_management import business_management_bp

def register_blueprints(app):
	app.register_blueprint(intro_bp)
	app.register_blueprint(home_bp)
	app.register_blueprint(buy_business_bp)
	app.register_blueprint(business_management_bp)