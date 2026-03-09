# 8. File Metadata Extractor

import os
import time


def get_file_metadata(directory_path):
    """Recursively walks through a directory and lists file metadata."""
    if not os.path.exists(directory_path):
        print("Directory path not found.")
        return

    print(f"{'Filename':<30} | {'Size (bytes)':<15} | {'Last Modified':<20}")
    print("-" * 75)

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Get file information
                file_info = os.stat(file_path)
                file_size = file_info.st_size
                last_modified = time.ctime(file_info.st_mtime)

                # Relative file name for better display
                rel_filename = os.path.relpath(file_path, directory_path)

                print(
                    f"{rel_filename[:30]:<30} | {file_size:<15} | {last_modified:<20}")
            except Exception as e:
                print(f"Error accessing file {file}: {e}")


def main():
    print("=== File Metadata Extractor ===")
    dir_path = input(
        "Enter directory path to scan (or '.' for current directory): ")
    dir_path = dir_path or "."
    get_file_metadata(dir_path)


if __name__ == "__main__":
    main()
