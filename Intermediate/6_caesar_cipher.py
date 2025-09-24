import string

def caesar_cipher(text, key, mode):
    """
    Encrypts or decrypts a message using the Caesar cipher.
    
    Args:
        text (str): The message to process.
        key (int): The integer shift key.
        mode (str): 'encrypt' or 'decrypt'.
        
    Returns:
        str: The processed message.
    """
    if mode == 'decrypt':
        key = -key

    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine the correct alphabet (uppercase or lowercase)
            alphabet = string.ascii_uppercase if char.isupper() else string.ascii_lowercase
            
            # Find the character's position and apply the shift
            original_pos = alphabet.find(char)
            shifted_pos = (original_pos + key) % 26
            
            result += alphabet[shifted_pos]
        else:
            # Keep non-alphabetic characters as they are
            result += char
            
    return result

if __name__ == "__main__":
    print("--- Basic Caesar Cipher ---")
    
    # 1. Get user input
    message = input("Enter your message: ")
    shift_key = int(input("Enter the shift key (an integer): "))
    process_mode = input("Do you want to 'encrypt' or 'decrypt'? ").lower()

    if process_mode in ['encrypt', 'decrypt']:
        # 2-6. Process and display the message
        processed_message = caesar_cipher(message, shift_key, process_mode)
        print(f"\nYour {process_mode}ed message is:\n{processed_message}")
    else:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")