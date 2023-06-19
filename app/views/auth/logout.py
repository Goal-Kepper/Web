from flask import Blueprint, session, flash, redirect, url_for
from app.views.auth.auth import login_required

logout_bp = Blueprint('logout', __name__)


@logout_bp.route('/logout')
@login_required
def logout():
    session.clear()
    flash('Вы вышли из аккаунта.')
    return redirect(url_for('auth.login.login'))