import os
import shutil

def organize_files(folder_path):
    # Get list of files in the specified folder
    files = os.listdir(folder_path)

    # Create a dictionary to store file extensions and corresponding folder names
    extension_folders = {
        ".txt": "TextFiles",
        ".pdf": "PDFFiles",
        ".jpg": "ImageFiles",
        ".png": "ImageFiles",
        ".xlsx": "ExcelFiles",
        ".docx": "WordFiles"
        # Add more file types and corresponding folder names as needed
    }

    # Iterate over each file
    for file in files:
        # Get the file extension
        _, extension = os.path.splitext(file)

        # If the file has an extension, move it to the corresponding folder
        if extension:
            # Create the folder if it doesn't exist
            folder_name = extension_folders.get(extension, "OtherFiles")
            folder_path = os.path.join(folder_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            # Move the file to the corresponding folder
            old_file_path = os.path.join(folder_path, file)
            new_file_path = os.path.join(folder_path, file)
            shutil.move(old_file_path, new_file_path)
            print(f"Moved {file} to {folder_name} folder.")

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to organize: ")
    organize_files(folder_path)
