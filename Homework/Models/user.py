from mongoengine import *

#design database
#create collection
class User(Document):
    name = StringField()
    email = StringField()
    username = StringField()
    password = StringField()
