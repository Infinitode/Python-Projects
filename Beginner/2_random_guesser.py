# Import the random module
import random

# Generate a random integer between 0 and 100
random_value = random.randint(0, 100)

# Ask for user input, and validate input
user_input = input("Enter your guess: ")
try:
    user_input = int(user_input)
    if user_input < 0 or user_input > 100:
        print("Please enter a number between 0 and 100.")
        exit()

except ValueError:
    print("Please enter a valid number.")
    exit()

# Display results if it is close, matches, or doesn't match
if user_input - 10 < random_value < user_input + 10:
    if user_input == random_value:
        print(f"Congratulations! You guessed the number {user_input} correctly!")
    else:
        print(f"You did it! You guessed the number {user_input}, the actual answer was {random_value}")
else:
    print(f"Sorry, you didn't guess the number. The actual answer was {random_value}")