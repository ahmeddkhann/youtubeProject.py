from connect import create_collection

def user_detail(name):
    try:
        collection = create_collection()
        user = collection.delete_one({"name": name})

        if user.deleted_count > 0:
            print("the user is deleted successfully")
        else:
            print("the user is not found")
    
    except Exception as e:
        print(f"An error occurred while deleting student data: {e}")


def delete_user():
    name = input("enter the student name to be deleted: ")
    user_detail(name)

#delete_user()