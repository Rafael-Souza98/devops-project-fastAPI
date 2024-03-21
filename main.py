from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine
from mongoengine import *

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': 'mongodb',
    'port': 27017,
    'username': 'admin',
    'password': 'admin'
}

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name', type=str, required=True, help="This field cannot be blank")
_user_parser.add_argument('last_name', type=str, required=True, help="This field cannot be blank")
_user_parser.add_argument('cpf', type=str, required=True, help="This field cannot be blank")
_user_parser.add_argument('email', type=str, required=True, help="This field cannot be blank")
_user_parser.add_argument('birthday_date', type=str, required=True, help="This field cannot be blank")


db = MongoEngine(app)
api = Api(app)

class UserModel(Document):
    cpf = StringField(required=True, unique=True, max_lenght=50)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    birthday_date = DateTimeField(required=True)


class User(Resource):
    def get(self, cpf):
        return {"CPF":cpf} #jsonify(UserModel.objects())
    
    def post(self):
        data = _user_parser.parse_args()
        UserModel(**data).delete()
        
    


api.add_resource(User, "/user")

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
