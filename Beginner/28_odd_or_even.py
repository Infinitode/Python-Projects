def check_odd_even(number):
    """
    Checks if a number is odd or even.
    """
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

if __name__ == "__main__":
    try:
        # 1. Prompt the user for a number
        user_input = input("Enter a number to check if it's odd or even: ")
        number = int(user_input)

        # 2. Check if it's odd or even
        result = check_odd_even(number)

        # 3. Display the result
        print(f"The number {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
