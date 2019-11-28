from dao import db, Base
from datetime import datetime


class PurchaseList(Base):
    __tablename__ = 'purchaseList'
    id = db.Column(db.Integer, primary_key=True)
    purchases = db.relationship('Purchase', back_populates='purchaseList')
    items = db.relationship('ItemPurchaseList', back_populates='purchaseList')
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
