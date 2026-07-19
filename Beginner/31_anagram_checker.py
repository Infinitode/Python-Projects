def check_anagram(str1, str2):
    """
    Checks if two strings are anagrams of each other.
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
    """
    # Remove whitespace and convert to lowercase for case-insensitive and clean comparison
    cleaned_str1 = "".join(str1.split()).lower()
    cleaned_str2 = "".join(str2.split()).lower()

    # If the lengths are not equal, they cannot be anagrams
    if len(cleaned_str1) != len(cleaned_str2):
        return False

    # Sort the characters of both strings and compare them
    # If the sorted characters are identical, the original strings are anagrams
    return sorted(cleaned_str1) == sorted(cleaned_str2)


if __name__ == "__main__":
    print("=== Anagram Checker ===")

    # 1. Prompt the user for two strings
    input_str1 = input("Enter the first word or phrase: ")
    input_str2 = input("Enter the second word or phrase: ")

    # 2. Process and check if they are anagrams
    is_anagram = check_anagram(input_str1, input_str2)

    # 3. Display the result
    if is_anagram:
        print(f"\nYes! '{input_str1}' and '{input_str2}' are anagrams of each other.")
    else:
        print(f"\nNo. '{input_str1}' and '{input_str2}' are not anagrams.")
