
from connect import create_collection

def user_details(name):
    
    try:
        collection = create_collection()
        user = collection.find_one({"name": name})

        if user:
                marks = int(input("enter marks of student to be updated: "))
                status = input("enter the student status to be updated: ")
                updated_data = collection.update_one({"name": name}, {"$set": {"marks": marks , "status": status}})
                print(f"data updated successfully and now {name} is {status} with {marks} marks")
                return updated_data
        else:
                return "user not found"

    except Exception as e:
        print(f"An error occurred while updating student data: {e}")


def update_user():

    print("Add the data of student to be updated")
    name = input("enter name of the student: ")

