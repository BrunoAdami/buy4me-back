from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from models.item import Item
from schemas.purchaseListSchema import PurchaseListSchema


class ItemSchema(ModelSchema):
    lists = fields.Nested('PurchaseListSchema', many=True)

    class Meta:
        model = Item
