# Get user email address
email = input("What is your email address?: ").strip()

# Slice out the user name
user_name = email[:email.index("@")]

# Slice out the domain name
domain_name = email[email.index("@")+1:]

# Format the message
output = f"Your username is '{user_name}' and your domain name is '{domain_name}'"

# Display the message
print(output)
