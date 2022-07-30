from sqlalchemy.orm import relationship
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    scrapes = db.relationship("Scrape", backref="user", lazy=True)


class Scrape(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    url = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    regex = db.Column(db.String(500))
    search_string = db.Column(db.String(500))

