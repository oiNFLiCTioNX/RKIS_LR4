from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, FileField, validators

class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Пароль', [
        validators.DataRequired(),
        validators.EqualTo('confirm_password', message='Пароли должны совпадать')
    ])
    confirm_password = PasswordField('Подтвердите пароль')

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя')  # Можно удалить, если не нужен
    email = StringField('Email')  # Новое поле
    password = PasswordField('Пароль')

class ProductForm(FlaskForm):
    title = StringField('Название', [validators.DataRequired()])
    description = TextAreaField('Описание', [validators.DataRequired()])
    version = StringField('Версия')
    file = FileField('Файл программы')