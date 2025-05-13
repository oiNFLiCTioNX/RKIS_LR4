from app import db
from flask_login import UserMixin
from enum import Enum
from passlib.hash import pbkdf2_sha256 as sha256

class Role(Enum):
    OWNER = "owner"
    ADMIN = "admin"
    MODERATOR = "moderator"
    DEVELOPER = "developer"
    USER = "user"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))
    role = db.Column(db.Enum(Role), default=Role.USER)

    def set_password(self, password):
        self.password = sha256.hash(password)

    def check_password(self, password):
        return sha256.verify(password, self.password)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.Text)
    version = db.Column(db.String(20))
    file_path = db.Column(db.String(200))
    approved = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))