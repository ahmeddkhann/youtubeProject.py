import pymongo

def connect ():
    try:
        uri = "mongodb+srv://iamahmedkhan02:databasePy@cluster0.5yobb.mongodb.net/"
        client = pymongo.MongoClient(uri)
        db = client["databsePy"]
        collection = db["users"]
        print(f"{db} is created successfully with collection name {collection}")
    except Exception as e :
        print("error while connecting to mongodb: ", e)
        

