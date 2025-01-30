import json

file_name = "youtube.txt"

def load_data():
    try:
        with open (file_name, "r") as file:
            return json.load(file) 
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open (file_name, "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    if not videos:
        print("No videos in the list")
    for index, video in enumerate(videos, start=1):
        print(f"index: {index},  video: {video}")

def add_video(videos):
    name = input("enter name of video ")
    time = input("enter duration of video ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    pass

def delete_video(videos):
    pass


def main():
    videos = load_data()
    while True:
        print(" ***** Youtube managemnt app *****")
        print("Choices you want to opearate.")
        print("1. list all the favourite videos.")
        print("2. Add new video.")
        print("3. Update video details.")
        print("4. Delete Video.")
        print("5. Exit.")

        choice = input("enter the choice: ")
        
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()