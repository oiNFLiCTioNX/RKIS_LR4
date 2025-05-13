from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
import os

from app import app, db
from app.models import Role, User, Product
from app.forms import RegisterForm, LoginForm, ProductForm

@app.route('/')
def index():
    products = Product.query.filter_by(approved=True).all()
    return render_template('index.html', products=products)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
     new_user = User(username=form.username.data)
     new_user.set_password(form.password.data)
     db.session.add(new_user)
     db.session.commit()
     flash("Вы зарегистрированы!")
     return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()

        print("Введённый логин:", username)
        print("Пользователь найден:", bool(user))

        if user:
            print("Хэш пароля из БД:", user.password)
            print("Проверка пароля:", user.check_password(password))

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('profile'))
        else:
            flash("Неверное имя пользователя или пароль")

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@app.route('/product/submit', methods=['GET', 'POST'])
@login_required
def submit_product():
    form = ProductForm()
    if form.validate_on_submit():
        f = form.file.data
        filename = secure_filename(f.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(path)

        product = Product(
            title=form.title.data,
            description=form.description.data,
            version=form.version.data,
            file_path=filename,
            user_id=current_user.id
        )
        db.session.add(product)
        db.session.commit()
        flash("Продукт отправлен на модерацию")
        return redirect(url_for('index'))
    return render_template('product_submit.html', form=form)

@app.route('/test-static')
def test_static():
    return '<link rel="stylesheet" href="/static/style.css">Открыл? Проверь консоль.'

@app.route('/debug-static')
def debug_static():
    from flask import current_app
    return {
        "static_folder": current_app.static_folder,
        "static_url_path": current_app.static_url_path
    }