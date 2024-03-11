from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine
from mongoengine import *

app = Flask(__name__)

app.config['MONGO_SETTINGS'] = {
    'db' : 'users',
    'host' : 'mongodb',
    'port' : 27017,
    'user' : 'admin',
    'password' : 'admin'
}


api = Api(app)
db = MongoEngine(app)

class User_Model(db.Document):
    cpf = StringField(required=True, unique=True, max_lenght=50)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    birth_date = DateTimeField(required=True)
    


class User(Resource):
    def get(self):
        return jsonify(User_Model._object_key) #corrigir
    
api.add_resource(User, "/user")

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)