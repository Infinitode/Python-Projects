# Imports
import string
import random

# Define the characters
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
all_characters = letters + digits + symbols

# Get the length of the password and validate it
length = input("Enter the length of the password: ")
try:
    length = int(length)
    if length < 8 or length > 128:
        print("Please enter a length between 8 and 128.")
        exit()
except ValueError:
    print("Please enter a valid number.")
    exit()

# Generate the password
password = ""

for i in range(length):
    password += random.choice(all_characters)

# Print the password
print(f"Your password is: {password}")