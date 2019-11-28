from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from models.purchaseList import PurchaseList
from schemas.itemPurchaseListSchema import ItemPurchaseListSchema
from schemas.purchaseSchema import PurchaseSchema


class PurchaseListSchema(ModelSchema):
    items = fields.Nested('ItemPurchaseListSchema', many=True)
    purchases = fields.Nested('PurchaseSchema', many=True)

    class Meta:
        model = PurchaseList
