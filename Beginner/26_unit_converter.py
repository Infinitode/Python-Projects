# 26. Unit Converter

def length_conversion(value, from_unit, to_unit):
    # Base unit: Meter
    conversions = {
        'meters': 1,
        'feet': 3.28084,
        'inches': 39.3701,
        'kilometers': 0.001,
        'miles': 0.000621371
    }

    if from_unit not in conversions or to_unit not in conversions:
        return None

    # Convert from input unit to meters
    meters = value / conversions[from_unit]
    # Convert from meters to target unit
    result = meters * conversions[to_unit]

    return result


def weight_conversion(value, from_unit, to_unit):
    # Base unit: Kilogram
    conversions = {
        'kilograms': 1,
        'pounds': 2.20462,
        'ounces': 35.274,
        'grams': 1000
    }

    if from_unit not in conversions or to_unit not in conversions:
        return None

    # Convert from input unit to kilograms
    kilograms = value / conversions[from_unit]
    # Convert from kilograms to target unit
    result = kilograms * conversions[to_unit]

    return result


def main():
    print("=== Unit Converter ===")
    print("1. Length (meters, feet, inches, kilometers, miles)")
    print("2. Weight (kilograms, pounds, ounces, grams)")

    choice = input("Select a conversion category (1-2): ")

    if choice == '1':
        value = float(input("Enter Value: "))
        from_unit = input("Convert from unit: ").lower()
        to_unit = input("Convert to unit: ").lower()
        result = length_conversion(value, from_unit, to_unit)
        if result is not None:
            print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")
        else:
            print("Invalid units.")
    elif choice == '2':
        value = float(input("Enter Value: "))
        from_unit = input("Convert from unit: ").lower()
        to_unit = input("Convert to unit: ").lower()
        result = weight_conversion(value, from_unit, to_unit)
        if result is not None:
            print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")
        else:
            print("Invalid units.")
    else:
        print("Invalid category.")


if __name__ == "__main__":
    main()
