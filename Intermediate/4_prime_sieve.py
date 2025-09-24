def sieve_of_eratosthenes(limit):
    """
    Finds all prime numbers up to a given limit using the Sieve of Eratosthenes.
    """
    # 2. Create a boolean list, initially all True
    primes = [True] * (limit + 1)
    
    # 3. Mark 0 and 1 as not prime
    if limit >= 0:
        primes[0] = False
    if limit >= 1:
        primes[1] = False

    # 4. Iterate and mark multiples
    for num in range(2, int(limit**0.5) + 1):
        if primes[num]:
            # Mark all multiples of num as not prime
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False

    # 5. Extract prime numbers
    prime_numbers = [i for i, is_p in enumerate(primes) if is_p]
    return prime_numbers

if __name__ == "__main__":
    print("--- Prime Number Sieve (Sieve of Eratosthenes) ---")
    try:
        # 1. Prompt user for an upper limit
        limit = int(input("Enter an upper limit to find prime numbers up to: "))
        if limit < 2:
            print("No prime numbers below 2.")
        else:
            prime_list = sieve_of_eratosthenes(limit)
            print(f"\nPrime numbers up to {limit} are:\n{prime_list}")
    except ValueError:
        print("Invalid input. Please enter a whole number.")