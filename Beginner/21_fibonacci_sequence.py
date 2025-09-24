def generate_fibonacci(n_terms):
    """
    Generates the Fibonacci sequence up to a certain number of terms.
    """
    # Handle edge cases for 0 or 1 term
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]

    # 3. Generate the sequence
    sequence = [0, 1]
    # Start the loop from the 3rd term since the first two are fixed
    while len(sequence) < n_terms:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    return sequence

if __name__ == "__main__":
    print("--- Fibonacci Sequence Generator ---")
    while True:
        try:
            # 1. Prompt user for the number of terms
            num_str = input("Enter the number of Fibonacci terms to generate: ")
            num_terms = int(num_str)

            if num_terms < 0:
                print("Please enter a non-negative number.")
                continue

            # 2. Call the function and 4. display the sequence
            fib_sequence = generate_fibonacci(num_terms)
            print(f"\nThe Fibonacci sequence with {num_terms} terms is:\n{fib_sequence}")
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")