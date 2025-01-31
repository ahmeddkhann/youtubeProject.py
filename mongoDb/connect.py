import pymongo

def connectToDb():
    try:
        uri = "mongodb+srv://iamahmedkhan02:databasePy@cluster0.5yobb.mongodb.net/"
        client = pymongo.MongoClient(uri)
        db = client["databasePy"]
        return db
    except Exception as e:
        print(f"Error connecting to database: {e}")
        
def create_collection():
        try:
            db = connectToDb()
            collection = db["users"]
            return collection
        except Exception as e:
            print(f"collection could not be created: {e}")