from connect import create_collection

def students_status():
     
     status = input("enter the status of the students you want to list. enter p for pass and f for fail: ")

     if status == "p" or status == "P":
          try:
               collection = create_collection()
               students = list(collection.find({"status": "pass"}, {"name":1, "marks":1, "status":1, "_id":0}))
               if students:
                    for student in students:
                         print(f"Name: {student.get('name')}, Marks: {student.get('marks')}, Status: {student.get('status')}" )
               else:
                    print("no student with the status of pass")
          except Exception as e:
               print(f"error while finding pass students: {e}")


     elif status == "f" or status == "F":
          try:
               collection = create_collection()
               students = list(collection.find({"status": "fail"}, {"name":1, "marks":1, "status":1, "_id":0}))
               if students:
                    for student in students:
                        print(f"Name: {student.get('name')}, Marks: {student.get('marks')}, Status: {student.get('status')}" )
               else:
                    print("no student with the status of pass")

          except Exception as e:
               print(f"error while finding fail students: {e}")

     else:
          print("invalid status. please enter p for pass or f for fail")

students_status()

          


     