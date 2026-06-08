def calculate_simple_interest(principal, rate, time):
    """
    Calculates simple interest.
    Formula: SI = (P * R * T) / 100
    """
    interest = (principal * rate * time) / 100
    return interest

if __name__ == "__main__":
    try:
        # 1. Get input for principal, rate, and time
        p = float(input("Enter the principal amount: "))
        r = float(input("Enter the annual interest rate (in %): "))
        t = float(input("Enter the time (in years): "))

        # 2. Calculate the interest
        si = calculate_simple_interest(p, r, t)

        # 3. Display the result
        print(f"\nThe simple interest is: {si}")
        print(f"Total amount (Principal + Interest): {p + si}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
