from dao import db, Base


class ItemPurchaseList(Base):
    __tablename__ = 'itemPurchaseList'
    purchase_list_id = db.Column(db.Integer, db.ForeignKey(
        'PurchaseList.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey(
        'item.id'), primary_key=True)
    price = db.Column(db.String(100))
    item = db.relationship(
        "Item", back_populates="purchaseList", uselist=False)
    purchase_list = db.relationship(
        "PurchaseList", back_populates="item", uselist=False)

    def __init__(self, price):
        self.price = price
