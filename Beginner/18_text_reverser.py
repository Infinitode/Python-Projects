def reverse_string(text):
    """
    Takes a string and returns it in reverse order.
    
    Args:
        text (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    # 3. Reverse the string using slicing
    return text[::-1]

if __name__ == "__main__":
    # 1. Prompt the user to enter a string
    user_input = input("Enter a string to reverse: ")
    # 2. Call the function with the user's input
    reversed_text = reverse_string(user_input)
    # 4. Display the reversed string
    print(f"The reversed string is: {reversed_text}")