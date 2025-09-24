def is_prime(num):
    """
    Checks if a number is prime.
    A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if num <= 1:
        return False
    # Check for divisors from 2 up to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes_up_to(limit):
    """
    Finds and returns a list of all prime numbers up to a specified limit.
    """
    prime_numbers = []
    # 3. Loop from 2 up to the limit
    for number in range(2, limit + 1):
        # 4. Check if the number is prime
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers

if __name__ == "__main__":
    print("--- Prime Number Generator ---")
    while True:
        try:
            # 1. Prompt the user for an upper limit
            limit_str = input("Enter an upper limit to find prime numbers up to: ")
            limit = int(limit_str)
            if limit < 2:
                print("Please enter a number greater than or equal to 2.")
                continue
            primes = generate_primes_up_to(limit)
            print(f"\nPrime numbers up to {limit} are:\n{primes}")
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")