def generate_acronym(phrase):
    """
    Generates an acronym from a given phrase.
    An acronym is an abbreviation formed from the initial letters of other words.
    """
    # Split the phrase into individual words using whitespace
    words = phrase.split()

    # Create an empty list to store the initial letters
    acronym_letters = []

    # Loop through each word in the phrase
    for word in words:
        # Check if the word contains alphabetic characters
        # Filter out numbers or special characters if needed
        # We take the first character of the word and capitalize it
        if word[0].isalpha():
            acronym_letters.append(word[0].upper())

    # Join the letters together into a single string
    acronym = "".join(acronym_letters)
    return acronym


if __name__ == "__main__":
    print("=== Acronym Generator ===")

    # 1. Prompt the user for a phrase
    user_phrase = input("Enter a phrase to generate its acronym: ")

    # 2. Process and generate the acronym
    if user_phrase.strip() == "":
        print("Please enter a valid non-empty phrase.")
    else:
        result_acronym = generate_acronym(user_phrase)

        # 3. Display the result
        if result_acronym:
            print(f"\nThe acronym for '{user_phrase}' is: {result_acronym}")
        else:
            print("\nCould not generate a valid acronym from the input.")
