from connect import create_collection

def user_details(name, address, age, marks, status):
        try:
            user = create_collection()
            user_data = {"name": name, "address": address, "age": age, "marks": marks, "status": status}
            resulted_data = user.insert_one(user_data)
            print(f"{name} with {marks} marks added successfully and is {status}")
            return resulted_data
        except Exception as e:
            print(f"User could not be added: {e}")


def add_user():

    print("Add the studeents details below to be added")
    name = input("Enter the name: ")
    address = input("Enter the address: ")
    age = int(input("Enter the age: "))
    marks = int(input("Enter the marks: "))
    status = input("Enter the status: ")

    user_details(name, address, age, marks, status)
