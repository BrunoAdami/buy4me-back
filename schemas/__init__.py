from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from models import Client, Item


class ClientSchema(ModelSchema):

    class Meta:
        model = Client

class ItemSchema(ModelSchema):

    class Meta:
        model = Item
