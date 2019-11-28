from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from models.purchase import Purchase
from schemas.clientSchema import ClientSchema
from schemas.purchaseListSchema import PurchaseListSchema
from schemas.deliverSchema import DeliverSchema


class PurchaseSchema(ModelSchema):
    client = fields.Nested('ClientSchema', many=False, only=['name'])
    deliver = fields.Nested('DeliverSchema', many=False, only=['name'])
    purchase_list = fields.Nested('PurchaseListSchema', many=False)

    class Meta:
        model = Purchase
