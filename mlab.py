import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds135290.mlab.com:35290/video

host = "ds135290.mlab.com"
port = 35290
db_name = "video"
user_name = "admin1"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
