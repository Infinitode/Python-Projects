import os
import shutil

def sort_files_in_directory(directory_path):
    """
    Organizes files in a directory into subfolders based on their file type.
    """
    # A dictionary to map file extensions to folder names
    # You can extend this with more file types
    file_type_mappings = {
        ".txt": "TextFiles",
        ".docx": "Documents",
        ".pdf": "PDFs",
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".mp3": "Music",
        ".mp4": "Videos",
        ".zip": "Archives",
    }

    # 1. Scan the directory for all files
    try:
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' was not found.")
        return

    if not files:
        print("No files to organize in this directory.")
        return

    # 2. For each file, move it to the appropriate folder
    for file in files:
        # 3. Get the file extension
        _, file_extension = os.path.splitext(file)
        
        # Determine the destination folder
        destination_folder_name = file_type_mappings.get(file_extension.lower(), "Other")
        destination_path = os.path.join(directory_path, destination_folder_name)

        # 4. Create the subfolder if it doesn't exist
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
            print(f"Created folder: {destination_folder_name}")

        # 5. Move the file
        source_file_path = os.path.join(directory_path, file)
        shutil.move(source_file_path, destination_path)
        print(f"Moved '{file}' to '{destination_folder_name}'")

    # 6. Display a summary
    print("\nFile organization complete!")

if __name__ == "__main__":
    # 1. Prompt the user for the directory path
    path_to_sort = input("Enter the directory path to organize: ")
    sort_files_in_directory(path_to_sort)