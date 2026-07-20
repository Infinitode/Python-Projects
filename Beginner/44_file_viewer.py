# made by @ericwasepic127

# import essentials 
import os

# first, let's create a 
# function that print file contents
def view_file(location):
    if not os.path.isfile(location):
        # in case when given path didn't exists or not file
        print(f"ERROR: File '{location}' doesn't exists or it's not file")
        return
        
    try: # just in case for any errors
        with open(location) as file: # no "r", but open's default is r!
            print("File:", location) # details
            print("-"*40) # separator 
            print(file.read()) # file contents 
    except PermissionError: # Permission failed to read
        print(f"ERROR: Failed to read file '{location}': Operation not permitted")
    except Exception as e: # any other errors occured 
        print("ERROR:", e)
        
# greets
print("Welcome to File viewer!")
print("Use 'exit' or Ctrl-C to exit")
print("You're at", os.getcwd(), "directory!")
print("In your folder, it has ...")
print("-", "\n- ".join(os.listdir()))

while location != "exit": # until user types exit
    try:
        location = input("\nEnter path to your file to view: ").strip().rstrip() # get location from user and clean spaces in front & end
        if location and location != "exit": # only when location received 
            view_file(location)
        elif location != "exit" or not location: # when it's not location, != for prove it's not exit too
            print("No location entered to view!") # say to user as didn't entered path
    except KeyboardInterrupt 
        break # exit got, break the loop
    except Exception as e:
        print("ERROR:", e)

print("Exit received! Bye!")

