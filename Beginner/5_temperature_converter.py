"""Convert between Celsius and Fahrenheit, respecting absolute zero."""

import math


ABSOLUTE_ZERO = {"C": -273.15, "F": -459.67}


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convert_temperature(temperature, unit):
    """Convert from C to F or F to C; reject physically impossible inputs."""
    unit = unit.strip().upper()
    if unit not in ABSOLUTE_ZERO:
        raise ValueError("Invalid unit of temperature")
    if not math.isfinite(temperature):
        raise ValueError("Please enter a finite temperature")
    if temperature < ABSOLUTE_ZERO[unit]:
        raise ValueError("Temperature below absolute zero")
    if unit == "C":
        return celsius_to_fahrenheit(temperature)
    return fahrenheit_to_celsius(temperature)


def main():
    unit = input("Enter the unit of temperature to convert from (C/F): ").strip().upper()
    try:
        temperature = float(input("Enter the temperature: "))
    except ValueError:
        print("Please enter a valid temperature")
        return

    try:
        converted = convert_temperature(temperature, unit)
    except ValueError as error:
        print(error)
        return

    other_unit = "F" if unit == "C" else "C"
    print(f"{temperature}°{unit} is {converted:.2f}°{other_unit}")


if __name__ == "__main__":
    main()
