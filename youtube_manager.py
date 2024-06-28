def load_data():
    # Sample data as the starting point
    return [
        {"name": "Sample Video 1", "time": "5:30"},
        {"name": "Sample Video 2", "time": "10:00"}
    ]

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, duration: {video['time']}")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = {"name": name, "time": time}
    else:
        print("Invalid index")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
    else:
        print("Invalid index")

def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager | Choose an option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        print(videos)

        match str(choice):
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
                print("Invalid input")

if __name__ == "__main__":
    main()