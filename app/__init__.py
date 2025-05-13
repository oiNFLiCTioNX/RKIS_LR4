from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app_dir = os.path.abspath(os.path.dirname(__file__))

# Получаем путь к корню проекта (RKIS_LR4/)
project_root = os.path.dirname(app_dir)

# Создаём приложение с правильными путями
app = Flask(__name__,
            static_folder=os.path.join(project_root, 'static'))

# Прописываем настройки напрямую — чтобы не зависеть от config.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123654cfc@localhost/RKIS_LR4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Папка для загрузок
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')

# Выводим диагностическую информацию
print("UPLOAD_FOLDER:", app.config['UPLOAD_FOLDER'])

# Инициализируем расширения
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Создаем папку uploads, если её нет
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Подключаем модели и маршруты
from app.models import Role, User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app import routes