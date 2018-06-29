import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds231360.mlab.com:31360/cms-app-c4e

host = "ds231360.mlab.com"
port = 31360
db_name = "cms-app-c4e"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
