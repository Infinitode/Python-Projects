def count_characters(text):
    """
    Counts vowels, consonants, digits, and special characters in a given text string.
    Returns a dictionary containing the counts for each category.
    """
    # Define set of vowels for quick lookup
    vowels = "aeiouAEIOU"

    # Initialize count variables
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    special_count = 0

    # Iterate through each character in the input text
    for char in text:
        if char.isalpha():
            # Check if alphabetic character is a vowel or consonant
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char.isdigit():
            # Check if character is a numeric digit
            digit_count += 1
        elif not char.isspace():
            # Any remaining non-whitespace character is categorized as special
            special_count += 1

    return {
        "vowels": vowel_count,
        "consonants": consonant_count,
        "digits": digit_count,
        "special": special_count,
    }


if __name__ == "__main__":
    print("=== Vowel & Consonant Counter ===")

    # 1. Prompt the user for text input
    user_input = input("Enter a sentence or phrase: ")

    # 2. Process and count character types
    results = count_characters(user_input)

    # 3. Display the results
    print("\n--- Character Count Summary ---")
    print(f"Vowels:             {results['vowels']}")
    print(f"Consonants:         {results['consonants']}")
    print(f"Digits:             {results['digits']}")
    print(f"Special Characters: {results['special']}")
