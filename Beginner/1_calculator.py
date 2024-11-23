# Function to validate the user's numeric input
def get_number(prompt):
    while True:
        # Get the user's input
        user_input = input(prompt)
        # Use a try block to catch errors during float conversion
        try:
            return float(user_input)  # Try converting input to a float
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Get and validate user input for the first and second numbers
number1 = get_number("Please enter the first number: ")
number2 = get_number("Please enter the second number: ")

# List the valid operations
valid_operations = ["add", "subtract", "multiply", "divide"]
while True:
    # Get the user's operation input
    operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()
    # Check if it's valid
    if operation in valid_operations:
        break
    else:
        # Invalid operation error
        print("Invalid operation. Please choose one of the following: add, subtract, multiply, divide.")

# Perform the chosen operation using if checks and store it for later
if operation == "add":
    result = number1 + number2
elif operation == "subtract":
    result = number1 - number2
elif operation == "multiply":
    result = number1 * number2
elif operation == "divide":
    # Handle division by zero
    if number2 != 0:
        result = number1 / number2
    else:
        result = "undefined (cannot divide by zero)"

# Display the result
print(f"The result of {operation}ing {number1} and {number2} is: {result}")