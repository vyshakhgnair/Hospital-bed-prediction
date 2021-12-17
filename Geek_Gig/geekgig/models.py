from datetime import datetime
from geekgig import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    data = db.relationship('DataA', backref='admin', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"

class Supplier(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    data = db.relationship('DataS', backref='supplier', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"


class DataA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    beds = db.Column(db.Integer, nullable=False)
    oxygen = db.Column(db.Integer, nullable=False)
    icu = db.Column(db.Integer, nullable=False)
    month_posted = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.month_posted}')"

class DataS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    beds = db.Column(db.Integer, nullable=False)
    oxygen = db.Column(db.Integer, nullable=False)
    icu = db.Column(db.Integer, nullable=False)
    month_posted = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.month_posted}')"