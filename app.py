from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.client_resource import ClientResource
from resources.item_resource import ItemResource
# from lista.resources.usuario_resource import UsuarioResource, UsuariosResource
# from lista.resources.lista_resource import ListaResource, ListasResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

app.secret_key = 'secreto'

# end of sqlalchemy configs
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})  # to use CORS

# create the database tables if they weren't allready created
@app.before_first_request
def create_tables():
    print("create tables")
    db.create_all()
# end of database creating

# api end-points:


api.add_resource(ClientResource, '/client', '/client/<string:username>')
api.add_resource(ItemResource, '/item', '/item/<string:name>')

# init database and run app
if __name__ == '__main__':
    from dao import db
    db.init_app(app)
    app.run(port=5000, debug=True)
