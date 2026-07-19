import sys
from pathlib import Path

def numput(prompt, default=0, convert_func=int, input_func=input):
    """Safely gets a numeric choice from the user, handling exit strings."""
    try:
        got = input_func(prompt).strip().lower()
        if got == 'exit':
            raise KeyboardInterrupt
        if not got:  # User just hit enter
            return default
        return convert_func(got)
    except ValueError:
        print("Non-numeric value entered. Using default option...")
        return default

def get_dir_contents(current_path: Path):
    """Separates files and folders accurately using pathlib."""
    files = []
    folders = []
    
    # path.iterdir() handles paths correctly without breaking on subdirectories
    for item in current_path.iterdir():
        if item.is_file():
            files.append(item.name)
        elif item.is_dir():
            folders.append(item.name)
            
    return sorted(files), sorted(folders)

def select_where_to_go(folders):
    """Displays choices and returns the folder name or '..' to go up."""
    # Create a local copy so we don't mutate the original folder list
    choices = list(folders)
    choices.append("..")  # Parent directory option
    
    menu = []
    for index, folder_name in enumerate(choices, start=1):
        if folder_name == "..":
            menu.append(f"{index}. Parent directory (..)")
        else:
            menu.append(f"{index}. Folder `{folder_name}`")
            
    print("\n".join(menu))
    
    total_options = len(choices)
    choice_idx = numput(f"Where to go (1~{total_options})? ", default=total_options)
    
    # Standard boundaries check
    if 1 <= choice_idx <= total_options:
        return choices[choice_idx - 1]
    
    print("Invalid choice. Staying in current directory.")
    return "."

def browse():
    """Main loop controller for navigating directories."""
    current_path = Path.cwd()
    
    print("Welcome to file explorer!")
    print("Ctrl-C or type 'exit' to quit.\n")
    
    while True:
        try:
            print(f"\nYou're at: {current_path}")
            files, folders = get_dir_contents(current_path)
            
            print("Files:")
            print(("- " + "\n- ".join(files)) if files else "- No files found")
            
            print("\nFolders:")
            if not folders and current_path == current_path.parent:
                print("- No folders found (and you are at the root directory).")
                # If we are at root and there are no folders, nowhere to go.
                break 
                
            destination = select_where_to_go(folders)
            
            # Resolve the new path safely
            next_path = (current_path / destination).resolve()
            
            if next_path.is_dir():
                current_path = next_path
            else:
                print("ERROR: Selected item is no longer a directory or is inaccessible.")
                
        except PermissionError:
            print("ERROR: Permission denied to access that directory.")
            # Safely fall back to the parent directory if stuck
            current_path = current_path.parent
        except KeyboardInterrupt:
            print("\nExit received. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    browse()
