from dao import db, Base


class ItemList(Base):
    __tablename__ = 'itemsLists'
    list_id = db.Column(db.Integer, db.ForeignKey(
        'lists.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey(
        'items.id'), primary_key=True)
    price = db.Column(db.String(100))
    item = db.relationship("Item", back_populates="lists", uselist=False)
    lista = db.relationship(
        "List", back_populates="items", uselist=False)

    def __init__(self, price):
        self.price = price
