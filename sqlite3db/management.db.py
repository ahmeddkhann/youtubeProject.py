import sqlite3

conn = sqlite3.connect("my_database.py")
cursor = conn.cursor()

cursor.execute('''
   CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
               )
 ''')

def list_videos():
    cursor.execute('''
                   SELECT * FROM videos''')
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute(''' 
        INSERT INTO videos (name, time) VALUES
                   (?, ?)''', (name, time))
    conn.commit()

def update_video(name, time, id):
    cursor.execute(''' 
        UPDATE videos SET name = ?, time = ? WHERE id = ? ''', 
        (name, time, id))
    conn.commit()

def delete_video(id):
    cursor.execute('''
        DELETE FROM videos WHERE id = ?''', (id,))
    conn.commit()


def main():
    
    while True:
        print("Youtube Management App with DB")
        print("Operations to be operated by your choice")
        print('1. List Videos')
        print('2. Add Videos')
        print('3. Update Videos')
        print('4. Delete Videos')
        print('5. Exit.')

        choice = int(input("enter the choice you want to operate"))

        if choice == 1:
            list_videos()

        elif choice == 2:
           name = input("enter name of video: ")
           time = input("enter duration of video: ")
           add_video(name, time)
        
        elif choice == 3:
            id = input("enter the id of video you want to update: ")
            name = input("enter name of new video: ")
            time = input("enter duration of new video: ")
            update_video(name, time, id)
        
        elif choice == 4:
            id = int(input("enter the id of video you want to delete: "))
            delete_video(id)

        elif choice == 5:
           break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()