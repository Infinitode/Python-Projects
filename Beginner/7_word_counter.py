# Get the input file path (TXT) from the user
file_path = input("Enter the file path (TXT): ")

# Read the file's content
with open(file_path, 'r', encoding='UTF-8') as file:
    content = file.read()

# Split the content into words
words = content.split()

# Count the number of words
word_count = len(words)

# Display the result
print(f"The file contains {word_count} words.")