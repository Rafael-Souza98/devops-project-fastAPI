
from mongoengine import *
from flask_mongoengine.wtf.orm import ModelForm

class UserModel(Document):
    cpf = StringField(required=True, unique=True, max_lenght=50)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    birthday_date = DateTimeField(required=True)