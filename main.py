from flask import Flask, jsonify
from flask_restful import Resource, Api
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
db = MongoEngine(app)
api = Api(app)

class UserModel(Document):
    cpf = StringField(required=True, unique=True, max_lenght=50)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    birth_date = DateTimeField(required=True)


class User(Resource):
    def get(self):
        return {"message":"user 1"} #jsonify(UserModel.objects())
    


api.add_resource(User, "/user")

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
