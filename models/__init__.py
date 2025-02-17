from dao import db, Base
from datetime import datetime


class Client(Base):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime)

    def __init__(self, username, email, name):
        self.username = username
        self.email = email
        self.name = name
        self.created_at = datetime.now()

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def fetch(cls):
        return cls.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Item(Base):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    price = db.Column(db.Float, unique=True)
    created_at = db.Column(db.DateTime)

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.created_at = datetime.now()

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def fetch(cls):
        return cls.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Deliver(Base):
    __tablename__ = 'deliver'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    score = db.Column(db.Float)
    available = db.Column(db.Boolean)
    vehicle_type = db.Column(db.String(30), nullable=False)
    vehicle_brand = db.Column(db.String(40), nullable=False)
    vehicle_year = db.Column(db.Integer, nullable=True)
    vehicle_plate = db.Column(db.String(20), nullable=True)
    # purchases = db.relationship('Purchase', back_populates='deliver')

    def __init__(self, username, email, name, score, available, vehicle_type,
                 vehicle_brand, vehicle_year, vehicle_plate):
        self.username = username
        self.email = email
        self.name = name
        self.score = score
        self.available = available
        self.vehicle_type = vehicle_type
        self.vehicle_brand = vehicle_brand
        self.vehicle_year = vehicle_year
        self.vehicle_plate = vehicle_plate

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_first_available(cls):
        return cls.query.filter_by(available=True).first()

    @classmethod
    def fetch(cls):
        return cls.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
