from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine


app = Flask(__name__)
api = Api(app)
db = MongoEngine(app)


app.config['MONGO_SETTINGS'] = {
    'db' : 'users',
    'host' : 'mongodb',
    'port' : 27017,
    'user' : 'admin',
    'password' : 'admin'
}

class User(Resource):
    def get(self):
        return {"message" : "user 1"}