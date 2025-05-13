import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'your-secret-key-here'

    # MySQL Настройки
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123654cfc'
    MYSQL_DB = 'RKIS_LR4'

    # SQLAlchemy URI
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Путь для загрузки файлов
    UPLOAD_FOLDER = os.path.join(basedir, 'static', 'uploads')