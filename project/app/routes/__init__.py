from .intro import intro_bp
from .home import home_bp

def register_blueprints(app):
	app.register_blueprint(intro_bp)
	app.register_blueprint(home_bp)
