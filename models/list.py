from dao import db, Base
from datetime import datetime


class List(Base):
    __tablename__ = 'lists'
    id = db.Column(db.Integer, primary_key=True)
    purchases = db.relationship('Purchase', back_populates='list')
    items = db.relationship('ItemList', back_populates='list')
    created_at = db.Column(db.DateTime)

    def __init__(self, purchases, items, created_at):
        self.purchases = purchases
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
