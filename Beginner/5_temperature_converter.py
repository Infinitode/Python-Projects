celsius_to_fahrenheit = lambda celsius: celsius * 9/5 + 32
fahrenheit_to_celsius = lambda fahrenheit: (fahrenheit - 32) * 5/9

user_unit = input("Enter the unit of temperature to convert from (C/F): ")
user_temperature = float(input("Enter the temperature: "))

try:
    if user_unit != "C" and user_unit != "F":
        raise ValueError("Invalid unit of temperature")
    if user_temperature < -273.15:
        raise ValueError("Temperature below absolute zero")
except ValueError as e:
    print(e)
    exit()

if user_unit == "C":
    print(f"{user_temperature}°C is {celsius_to_fahrenheit(user_temperature):.2f}°F")
elif user_unit == "F":
    print(f"{user_temperature}°F is {fahrenheit_to_celsius(user_temperature):.2f}°C")