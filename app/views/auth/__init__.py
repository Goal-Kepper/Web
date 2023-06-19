from app.views.auth.login import login_bp
from app.views.auth.logout import logout_bp
from app.views.auth.register import register_bp
from app.views.auth.auth import auth_bp

auth_bp.register_blueprint(login_bp)
auth_bp.register_blueprint(logout_bp)
auth_bp.register_blueprint(register_bp)