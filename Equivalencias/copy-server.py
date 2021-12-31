import pymongo
import pprint

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

dblist = myclient.list_database_names()
if "equivalencias-py" in dblist:
    # mydb = myclient["equivalencias"]
    newdb = myclient["equivalencias-py"]
    #mycol = mydb["processos"]
    #for x in mycol.find():
    #   newdb.processos.insert_one(x)
    
    newcol = newdb.processos
    for x in newcol.find():
        pprint.pprint(x)