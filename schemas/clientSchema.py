from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from models.client import Client
from schemas.purchaseSchema import PurchaseSchema


class ClientSchema(ModelSchema):
    purchases = fields.Nested('PurchaseSchema', many=True)

    class Meta:
        model = Client
