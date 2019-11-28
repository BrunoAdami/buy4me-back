from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from models.deliver import Deliver
from schemas.purchaseSchema import PurchaseSchema


class DeliverSchema(ModelSchema):
    purchases = fields.Nested('PurchaseSchema', many=True)

    class Meta:
        model = Deliver
