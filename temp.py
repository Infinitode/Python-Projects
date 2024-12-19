operation = input("Type your operation: ")
number1 = float(input("Type your first number: "))
number2 = float(input("Type your second number: "))

result = 0

if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    if number2 == 0:
        print("Cannot divide by zero. It is undefined.")
        exit()
    else:
        result = number1 / number2
else:
    print("Invalid operation")
    exit()

print(f"Your operation was: {number1} {operation} {number2} = {result}")