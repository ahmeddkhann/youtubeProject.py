from add_user import add_user
from delete_user import delete_user
from update_user import update_user
from list_students import students_status

def main ():

    while True:
        print("List of the operations to be operated: ")
        print("1. Add user")
        print("2. List of Students")
        print("3. Update user")
        print("4. Delete user")
        print("5. Exit")

        choose = input("no. of the operation you want to operate: ")
        if choose == "1":
            add_user()
        elif choose == "2":
            students_status()
        elif choose == "3":
            update_user()
        elif choose == "4":
            delete_user()
        elif choose == "5":
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please choose a valid option")


if __name__ == "__main__":
    main()