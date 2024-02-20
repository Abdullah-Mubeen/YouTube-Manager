import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []

def save_helper_method(videos):
        with open('youtube.txt', 'w') as file:
            json.dump(videos, file)
    

def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*"*70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_helper_method(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to Update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_helper_method(videos)
    else:
        print("Invalid Index selected")



def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_helper_method(videos)
    else:
        print("Invalid Index selected")
    


def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all Youtube videos ")
        print("2. Add a Youtube video ")
        print("3. Update a Youtube video Detail ")
        print("4. Delete a Youtube video ")
        print("5. Exit the app ")
        choise = int(input("Enter your choise: "))
        # print(videos)


        match choise:
            case 1:
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                break
            case _:
                print("Invalid Choise")


if __name__ == "__main__":
    main()



















