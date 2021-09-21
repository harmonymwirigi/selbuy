from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_email):
    return User_1.query.get(int(user_email))


class User_1(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    second_name = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    confirm_password = db.Column(db.String, nullable=False)
    sales = db.relationship('Sales', backref='seller', lazy=True)

    __table_args__ = {'extend_existing': True}


class Sales(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    quantity = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    picture = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('user_1.id'), nullable=False)

    __table_args__ = {'extend_existing': True}
