# Get the user's input text
text = input("Enter the text you want to encrypt: ")

# Get the user's encryption password
password = input("Enter the password to encrypt the text: ")

# Encrypt the text using Caesar cipher
encrypted_text = ""
for char in text:
    encrypted_text += chr(ord(char) + len(password))

# Print the encrypted text
print("Encrypted text:", encrypted_text)

decrypt = input("Do you want to decrypt the text? (yes/no): ")
if decrypt == "yes":
    # Decrypt the text using Caesar cipher
    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text += chr(ord(char) - len(password))

    # Print the decrypted text
    print("Decrypted text:", decrypted_text)