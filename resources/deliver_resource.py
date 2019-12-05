from flask_restful import Resource, reqparse, abort
from flask import request
from models import Deliver
from schemas import DeliverSchema


class DeliverResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='o username do Entregador não pode ficar em branco'
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help='O email do Entregador não pode estar em branco'
                        )
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='O name do Entregador não pode estar em branco'
                        )
    parser.add_argument('score',
                        type=float,
                        required=True,
                        help='O score do Entregador não pode estar em branco'
                        )
    parser.add_argument('available',
                        type=bool,
                        required=True,
                        help='A disponibilidade do Entregador não pode estar em branco'
                        )
    parser.add_argument('vehicle_type',
                        type=str,
                        required=True,
                        help='O tipo do veículo do Entregador não pode estar em branco'
                        )
    parser.add_argument('vehicle_brand',
                        type=str,
                        required=False
                        )
    parser.add_argument('vehicle_year',
                        type=int,
                        required=False
                        )
    parser.add_argument('vehicle_plate',
                        type=str,
                        required=False
                        )

    def get(self, username):
        json = ''
        try:
            deliver = Deliver.find_by_username(username)
            print(deliver)
            if deliver:
                schema = DeliverSchema()
                json = schema.dump(deliver)
            else:
                return {"message": "Entregador {} não existe".format(username)}, 500
        except Exception as e:
            print(e)
            return {"message": "Erro na requisição".format(username)}, 500
        return json, 200

    def post(self):
        try:
            data = DeliverResource.parser.parse_args()
            if not data:
                return {"message": "Requisição sem JSON"}, 400

            if Deliver.find_by_username(data['username']):
                return {"message": "Usuário ja existe"}, 400
            else:
                deliver = Deliver(data['username'], data['email'], data['name'],
                                  data['score'], data['available'], data['vehicle_type'],
                                  data['vehicle_brand'], data['vehicle_year'], data['vehicle_plate'])
                deliver.add()
                deliver = Deliver.find_by_username(data['username'])

                deliver_schema = DeliverSchema()
                json = deliver_schema.dump(deliver)
                return json, 201

        except Exception as ex:
            print(ex)
            return {"message": "erro"}, 500


class AvailableDeliverResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='o username do Entregador não pode ficar em branco'
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help='O email do Entregador não pode estar em branco'
                        )
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='O name do Entregador não pode estar em branco'
                        )
    parser.add_argument('score',
                        type=float,
                        required=True,
                        help='O score do Entregador não pode estar em branco'
                        )
    parser.add_argument('available',
                        type=bool,
                        required=True,
                        help='A disponibilidade do Entregador não pode estar em branco'
                        )
    parser.add_argument('vehicle_type',
                        type=str,
                        required=True,
                        help='O tipo do veículo do Entregador não pode estar em branco'
                        )
    parser.add_argument('vehicle_brand',
                        type=str,
                        required=False
                        )
    parser.add_argument('vehicle_year',
                        type=int,
                        required=False
                        )
    parser.add_argument('vehicle_plate',
                        type=str,
                        required=False
                        )

    def get(self):
        json = ''
        try:
            deliver = Deliver.find_first_available()
            print(deliver)
            if deliver:
                schema = DeliverSchema()
                json = schema.dump(deliver)
            else:
                return {"message": "Entregador {} não existe".format(username)}, 500
        except Exception as e:
            print(e)
            return {"message": "Erro na requisição".format(username)}, 500
        return json, 200
