from flask_restful import Resource, reqparse, abort
from flask import request
from models import Item
from schemas import ItemSchema


class ItemResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='o nome do Item não pode ficar em branco'
                        )
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='o preco do Item não pode ficar em branco'
                        )

    def get(self, name):
        json = ''
        try:
            item = Item.find_by_name(name)
            print(item)
            if item:
                schema = ItemSchema()
                json = schema.dump(item)
            else:
                return {"message": "Item {} não existe".format(name)}, 500
        except Exception as e:
            print(e)
            return {"message": "Erro na requisição".format(name)}, 500
        return json, 200

    def post(self):
        try:
            data = ItemResource.parser.parse_args()
            if not data:
                return {"message": "Requisição sem JSON"}, 400

            if Item.find_by_name(data['name']):
                return {"message": "Item ja existe"}, 400
            else:
                item = Item(data['name'], data['price'])
                item.add()
                item = Item.find_by_name(data['name'])

                item_schema = ItemSchema()
                json = item_schema.dump(item)
                return json, 201

        except Exception as ex:
            print(ex)
            return {"message": "erro"}, 500
