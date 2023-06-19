# Описание основных функций, общих для обоих экранов

from flask import (Blueprint, g, session, redirect, url_for)
import functools

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

MIN_LOGIN_LENGTH = 4
MAX_LOGIN_LENGTH = 32

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 16

ADMIN_LOGIN = 'student'
ADMIN_PASSWORD = 'P@ssword'

LOGIN_URL_API = 'http://127.0.0.1:5000/log'
REGISTER_URL_API = 'http://127.0.0.1:5000/reg'


def is_logged_in():
    login = session.get('login', None)
    role = session.get('role', None)

    g.login = login
    g.role = role


def has_role(role):
    def wrapped_func(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            if role == g.role:
                return view(**kwargs)
            return 'У вас недостаточно прав для доступа к этой странице'
        return wrapped_view
    return wrapped_func


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.login is None:
            return 'Для начала вы должны быть авторизованы'
        return view(**kwargs)
    return wrapped_view


def logout_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.login is not None:
            return 'Для доступа к этой странице выйдите из аккаунта'
        return view(**kwargs)
    return wrapped_view
