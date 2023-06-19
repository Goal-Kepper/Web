from wtforms import Form, StringField, EmailField, PasswordField
from wtforms.validators import Length, EqualTo, InputRequired
from app.views.auth.auth import (MIN_LOGIN_LENGTH, MAX_LOGIN_LENGTH, MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH)


class RegisterForm(Form):
    login = StringField('Логин', validators=[InputRequired(), Length(min=MIN_LOGIN_LENGTH, max=MAX_LOGIN_LENGTH)])
    email = EmailField('Почта', validators=[InputRequired()])
    password = PasswordField('Пароль',
                             validators=[InputRequired(), Length(min=MIN_PASSWORD_LENGTH, max=MAX_PASSWORD_LENGTH),
                                         EqualTo('password_confirm', message='Пароли должны совпадать')])
    password_confirm = PasswordField('Подтверждение пароля', validators=[InputRequired()])
