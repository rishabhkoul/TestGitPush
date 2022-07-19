import pymongo
import urllib

client = pymongo.MongoClient("mongodb+srv://Rishabh:" + urllib.parse.quote("Zenfone@2") + "@cluster0.lhaw5.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {"name": "Rohit", "email": "rohit@gmail.com", "surname": "Raina"}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)