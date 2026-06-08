def generate_table(number, table_range=10):
    """
    Generates a multiplication table for a given number.
    """
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, table_range + 1):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    try:
        # 1. Prompt the user for a number
        num = int(input("Enter the number for the multiplication table: "))

        # 2. Prompt for range (optional, defaults to 10)
        range_input = input("Enter the range (default is 10): ")
        if range_input.strip() == "":
            generate_table(num)
        else:
            generate_table(num, int(range_input))

    except ValueError:
        print("Invalid input. Please enter integers.")
