from .intro import intro_bp

def register_blueprints(app):
	app.register_blueprint(intro_bp)
