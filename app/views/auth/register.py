import requests
import json
from flask import (Blueprint, render_template, request, redirect, url_for, flash)
from app.views.auth.register_forms import RegisterForm
from app.views.auth.auth import logout_required
from app.views.auth.auth import REGISTER_URL_API

register_bp = Blueprint('register', __name__, template_folder='templates', static_folder='static',
						static_url_path='/static/register')

@register_bp.route('/register', methods=['GET', 'POST'])
@logout_required
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		login = form.login.data
		email = form.email.data
		password = form.password.data

		send_data = {'login': login, 'email': email, 'password': password}

		response = requests.post(REGISTER_URL_API, json=json.dumps(send_data))

		if response.status_code == 201:
			flash('Вы успешно зарегистрировались! Пройдите авторизацию.')
			return redirect(url_for('auth.login.login'))
		else:
			flash('Что-то пошло не так. Повторите попытку!')
			return redirect(url_for('auth.register.register'))

	return render_template('register_page/register.html', form=form)
