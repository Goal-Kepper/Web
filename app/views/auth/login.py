import requests
import json
from flask import (Blueprint, render_template, request, redirect, url_for, flash, session)
from app.views.auth.login_forms import LoginForm
from app.views.auth.auth import LOGIN_URL_API, ADMIN_LOGIN, ADMIN_PASSWORD
from app.views.auth.auth import logout_required
from app.views.auth.roles import CLIENT_ROLE, ADMIN_ROLE

login_bp = Blueprint('login', __name__, template_folder='templates', static_folder='static', static_url_path='/static/login')


@login_bp.route('/login', methods=['GET', 'POST'])
@logout_required
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        login = form.login.data
        password = form.password.data

        if login == ADMIN_LOGIN and password == ADMIN_PASSWORD:
            session['login'] = login
            session['role'] = ADMIN_ROLE
            return 'Вы успешно авторизованы в качестве админа'

        send_data = {'login': login, 'password': password}
        response = requests.post(LOGIN_URL_API, json=json.dumps(send_data))

        if response.status_code == 201:
            session['login'] = login
            session['role'] = CLIENT_ROLE
            return 'Вы успешно авторизованы'
        else:
            flash('Ошибка авторизации!')
            return redirect(url_for('auth.login.login'))

    return render_template('login_page/login.html', form=form)
