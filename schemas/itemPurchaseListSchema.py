from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from models.itemPurchaseList import ItemPurchaseList
from schemas.itemSchema import ItemSchema


class ItemPurchaseListSchema(ModelSchema):
    item = fields.Nested('ItemSchema', many=False, only=['name'])

    class Meta:
        model = ItemPurchaseList
