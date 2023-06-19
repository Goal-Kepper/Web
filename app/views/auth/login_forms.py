from wtforms import Form, StringField, PasswordField
from wtforms.validators import InputRequired, Length
from app.views.auth.auth import (MIN_LOGIN_LENGTH, MAX_LOGIN_LENGTH, MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH)


class LoginForm(Form):
    login = StringField('Логин', validators=[InputRequired(), Length(min=MIN_LOGIN_LENGTH, max=MAX_LOGIN_LENGTH)])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=MIN_PASSWORD_LENGTH, max=MAX_PASSWORD_LENGTH)])
