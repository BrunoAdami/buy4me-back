from flask_restful import Resource, reqparse, abort
from flask import request
from models import PurchaseList, ItemPurchaseList, Item
from schemas import PurchaseListSchema


class PurchaseListResource (Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('items',
                        type=dict, location='json', action='append',
                        required=True,
                        help='Os Itens não pode estar em branco.'
                        )

    def post(self):
        json = ''
        try:
            data = PurchaseListResource.parser.parse_args()
            if not data:
                return {"mensagem": "A requisição não tem dados JSON"}, 400
            # purchase_list = PurchaseList.find_by_id(id=data["id"])
            # if purchase_list:
            #     return {"mensagem": "Uma lista já existe com esse id"}, 400

            list_items = data['items']
            purchase_list = PurchaseList()

            for single_item in list_items:
                item_list_connector = ItemPurchaseList()
                item_in_database = Item.find_by_name(single_item['name'])
                if not item_in_database:
                    raise Exception(
                        'Item {} não encontrado no banco de dados'.format(single_item['name']))
                item_list_connector.item = item_in_database
                purchase_list.append(item_list_connector)
            purchase_list.add()
            purchase_id = purchase_list.id
            purchase_list = PurchaseList.find_by_id(_id=purchase_id)
            schema = PurchaseListSchema()
            json = schema.dump(purchase_list)
        except Exception as e:
            print(e)
            abort(500, message="Erro no POST")
        return json, 201

    def get(self, _id):
        json = ''
        try:
            purchase_lists = PurchaseList.fetch()
            schema = PurchaseListSchema(many=True)
            json = schema.dump(purchase_lists)
        except Exception as e:
            print(e)
            return {"message": "Aconteceu um erro tentando retornar as listas de compras do Banco de Dados."}, 500
        return json, 200
