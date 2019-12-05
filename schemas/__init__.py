from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from models import Client


class ClientSchema(ModelSchema):

    class Meta:
        model = Client
