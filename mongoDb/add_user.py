from connect import connectToDb

def main():

    def create_collection():
        try:
            db = connectToDb()
            collection = db["users"]
            return collection
        except Exception as e:
            print(f"collection could not be created: {e}")

    def add_user():
        try:
            pass
        except Exception as e:
            print(f"User could not be added: {e}")
    
    add_user()

if __name__ == "__main__":
    main()