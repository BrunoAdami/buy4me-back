from dao import db, Base
from datetime import datetime


class Client(Base):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    purchases = db.relationship('Purchase', back_populates='client')
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


# We don't need to define a __init__ method because SQLAlchemy adds an
# implicit constructor to all model classes which accepts keyword arguments
# for all its columns and relationships.
