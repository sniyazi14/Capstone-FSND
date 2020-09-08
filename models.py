from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path = os.environ['DATABASE_URL']
# conn = psycopg2.connect(database_path, sslmode='require')
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


# Advisors model
class Advisor(db.Model):
    __tablename__ = 'advisors'
    id = Column(db.Integer, primary_key=True)
    first_name = Column(db.String)
    last_name = Column(db.String)
    field = Column(db.String)
    position = Column(db.String)
    experience = Column(db.Integer)
    country = Column(db.String)

    def __init__(self, first_name, last_name, field,
                 position, experience, country):
        self.first_name = first_name
        self.last_name = last_name
        self.field = field
        self.position = position
        self.experience = experience
        self.country = country

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def fetch(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'field': self.field,
            'position': self.position,
            'experience': self.experience,
            'country': self.country
        }


# Users Model
class User(db.Model):
    __tablename__ = 'users'
    id = Column(db.Integer, primary_key=True)
    first_name = Column(db.String)
    last_name = Column(db.String)
    field = Column(db.String)
    level = Column(db.Integer)
    subscription_active = Column(db.Boolean, default=False)
    advisor_name = Column(db.String)

    def __init__(self, first_name, last_name, field,
                 level, subscription_active, advisor_name):
        self.first_name = first_name
        self.last_name = last_name
        self.field = field
        self.level = level
        self.subscription_active = subscription_active
        self.advisor_name = advisor_name

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def fetch(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'field': self.field,
            'level': self.level,
            'subscription_active': self.subscription_active,
            'advisor_name': self.advisor_name
        }
