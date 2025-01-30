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

    print("/n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index},  {video['name']}, duration: {video["time"]}")
    print("/n")
    print("*" * 70)


def add_video(videos):
    name = input("enter name of video ")
    time = input("enter duration of video ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("enter the video number to be update "))
    if 1 <= index <= len(videos):
        name = input("enter name of the new video: ")
        time = input("enter duration of the new video")
        videos[index-1] = {"name": name, "time":time }
        save_data_helper(videos)
    else:
        print("you have entered an invalid index")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("enter the video number you want to delete "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
    else:
        print("you have entered an invalid index")

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