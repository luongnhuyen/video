from mongoengine import *
from Models.service import Service
from Models.user import User

#design database
#create collection
class Order(Document):
    nameservice = ReferenceField(Service, required=True)
    username = ReferenceField(User, required=True)
    time = DateTimeField()
    is_accepted = BooleanField()
