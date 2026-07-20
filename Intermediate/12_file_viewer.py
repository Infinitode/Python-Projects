# made by @ericwasepic127 (Fixed)

import os
import sys

def view_file(location):
    if not os.path.isfile(location):
        print(f"ERROR: File '{location}' doesn't exist or it's a directory.")
        return

    try:
        # Added utf-8 encoding to prevent crash on special characters
        with open(location, mode='r', encoding='utf-8') as file:
            print("File:", location) 
            print("-" * 40) 
            print(file.read()) 
    except PermissionError: 
        print(f"ERROR: Failed to read file '{location}': Operation not permitted")
    except UnicodeDecodeError:
        print(f"ERROR: Cannot read '{location}'. It might be a binary file (like an image or executable) or use a non-UTF-8 encoding.")
    except Exception as e: 
        print("ERROR:", e)

print("Welcome to File viewer!")
print("Use 'exit' or Ctrl-C to exit")
print("You're at", os.getcwd(), "directory!")
print("In your folder, it has ...")

try:
    print("- " + "\n- ".join(os.listdir()))
except Exception as e:
    print("- (Unable to list directory contents)")

# FIX: Initialize the variable so the while loop doesn't crash on start
location = ""

while location != "exit": 
    try:
        location = input("\nEnter path to your file to view: ").strip()
        
        if not location:
            print("No location entered to view!")
            continue
            
        if location != "exit": 
            view_file(location)
            
    # FIX: Added the missing colon
    except KeyboardInterrupt: 
        print() # Clean newline after Ctrl+C
        break 
    except Exception as e:
        print("ERROR:", e)

print("Exit received! Bye!")