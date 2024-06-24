import os
import shutil

def create_folder(directory, folder_name):
    folder_path = os.path.join(directory, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def get_file_type(file_name):
    return file_name.split('.')[-1] if '.' in file_name else 'others'

def organize_files(directory_path):
    if not os.path.exists(directory_path):
        print(f"The directory {directory_path} does not exist.")
        return

    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    
    if not files:
        print("The directory is empty.")
        return

    for file in files:
        file_type = get_file_type(file)
        folder_path = create_folder(directory_path, file_type)
        shutil.move(os.path.join(directory_path, file), os.path.join(folder_path, file))
    
    print(f"Files have been organized in {directory_path}")

if __name__ == "__main__":
    directory_path = input("Enter a folder path you want to manage: ")
    organize_files(directory_path)
