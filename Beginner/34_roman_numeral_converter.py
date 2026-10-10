def int_to_roman(number):
    """Convert an integer from 1 to 3999 to its canonical Roman numeral."""
    if isinstance(number, bool) or not isinstance(number, int) or not 1 <= number <= 3999:
        raise ValueError("Number must be an integer between 1 and 3999.")

    # Mapping of integer values to Roman numeral symbols in descending order
    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    result = []
    for value, symbol in roman_map:
        # Append symbol while number is greater than or equal to value
        while number >= value:
            result.append(symbol)
            number -= value

    return "".join(result)


def roman_to_int(roman_str):
    """Convert a canonical Roman numeral (case-insensitive) to an integer."""
    # Mapping of single Roman numeral characters to integer values
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    roman_str = roman_str.upper().strip()
    total = 0
    prev_value = 0

    # Process characters from right to left
    for char in reversed(roman_str):
        if char not in roman_values:
            raise ValueError(f"Invalid Roman numeral character: '{char}'")

        current_value = roman_values[char]

        # If current value is less than previous value, subtract it (e.g., IV -> 5 - 1 = 4)
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
            prev_value = current_value

    # Round-tripping rejects illegal repetitions/subtractions (IIII, IC, etc.)
    # and values outside the conventional 1-3999 range.
    if not 1 <= total <= 3999 or int_to_roman(total) != roman_str:
        raise ValueError("Invalid Roman numeral: '{}'".format(roman_str))
    return total


if __name__ == "__main__":
    print("=== Roman Numeral Converter ===")
    print("1. Convert Integer to Roman Numeral")
    print("2. Convert Roman Numeral to Integer")

    choice = input("Select an option (1 or 2): ").strip()

    if choice == "1":
        try:
            num = int(input("Enter an integer (1 - 3999): "))
            if 1 <= num <= 3999:
                roman = int_to_roman(num)
                print(f"\nThe Roman numeral for {num} is: {roman}")
            else:
                print("Number must be between 1 and 3999.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    elif choice == "2":
        roman_input = input("Enter a Roman numeral (e.g., XIV): ")
        try:
            integer_val = roman_to_int(roman_input)
            print(f"\nThe integer value for '{roman_input.upper()}' is: {integer_val}")
        except ValueError as e:
            print(f"Error: {e}")

    else:
        print("Invalid choice. Please enter 1 or 2.")
