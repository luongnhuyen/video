import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds119660.mlab.com:19660/muadongkhonglanh

host = "ds119660.mlab.com"
port = 19660
db_name = "muadongkhonglanh"
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
