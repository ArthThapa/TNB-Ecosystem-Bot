from tinydb import TinyDB, Query
db = TinyDB("servers.json")
server = Query()

for i in db.all()[:3]:
    print(f"{i['server_name']} {i['server_id']}")