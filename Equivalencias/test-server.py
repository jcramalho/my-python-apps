import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

dblist = myclient.list_database_names()
if "equivalencias" in dblist:
    mydb = myclient["equivalencias"]
    print(mydb.list_collection_names())
