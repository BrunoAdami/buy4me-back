from dao import db, Base
from datetime import datetime


class Purchase(Base):
    __tablename__ = 'purchase'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey(
        'client.id'), nullable=False)
    client = db.relationship('Client', back_populates='purchase')
    purchase_list_id = db.Column(
        db.Integer, db.ForeignKey('purchaseList.id'), nullable=False)
    purchase_list = db.relationship('PurchaseList', back_populates='purchase')
    deliver_id = db.Column(db.Integer, db.ForeignKey(
        'deliver.id'), nullable=False)
    deliver = db.relationship('Deliver', back_populates='purchase')

    def __init__(status, client_id, purchase_list_id, deliver_id):
        self.status = status
        self.client_id = client_id
        self.purchase_list_id = purchase_list_id
        self.deliver_id = deliver_id

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
