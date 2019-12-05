from flask_restful import Resource, reqparse, abort
from flask import request
from models import Client
from schemas import ClientSchema


class ClientResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='o nome do Cliente não pode ficar em branco'
                        )
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='O username do Cliente não pode estar em branco'
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help='O email do Cliente não pode estar em branco'
                        )

    def get(self, username):
        json = ''
        try:
            client = Client.find_by_username(username)
            print(client)
            if client:
                schema = ClientSchema()
                json = schema.dump(client)
            else:
                return {"message": "Cliente {} não existe".format(username)}, 500
        except Exception as e:
            print(e)
            return {"message": "Erro na requisição".format(username)}, 500
        return json, 200

    def post(self):
        try:
            data = ClientResource.parser.parse_args()
            if not data:
                return {"message": "Requisição sem JSON"}, 400

            if Client.find_by_username(data['username']):
                return {"message": "Usuário ja existe"}, 400
            else:
                client = Client(data['username'], data['email'], data['name'])
                client.add()
                client = Client.find_by_username(data['username'])

                client_schema = ClientSchema()
                json = client_schema.dump(client)
                return json, 201

        except Exception as ex:
            print(ex)
            return {"message": "erro"}, 500
