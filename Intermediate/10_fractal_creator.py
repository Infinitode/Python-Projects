# 10. Fractal Creator

def generate_mandelbrot(width, height, max_iterations):
    """
    Generates and prints a Mandelbrot set fractal in ASCII art.
    Each coordinate (x, y) is mapped to a complex number c = x + iy.
    Iterating z_next = z^2 + c determines if the point remains bounded or escapes to infinity.
    """
    # Character list to represent density/iteration depth (from densest to lightest/empty)
    chars = "@%#*+=-:. "

    # Define the range of the complex plane to display
    x_min, x_max = -2.0, 0.5
    y_min, y_max = -1.2, 1.2

    # Loop through each row (height)
    for y_idx in range(height):
        # Map row index to imaginary part of complex number c
        # (inverted so top rows correspond to positive imaginary values)
        # Avoid division by zero if height is 1
        denominator_y = (height - 1) if height > 1 else 1
        imaginary = y_min + (y_max - y_min) * (height - 1 - y_idx) / denominator_y

        row_output = []
        # Loop through each column (width)
        for x_idx in range(width):
            # Map column index to real part of complex number c
            # Avoid division by zero if width is 1
            denominator_x = (width - 1) if width > 1 else 1
            real = x_min + (x_max - x_min) * x_idx / denominator_x

            # Define complex number c
            c = complex(real, imaginary)
            z = 0j

            # Iterate the formula z = z^2 + c up to max_iterations
            iteration = 0
            while abs(z) <= 2.0 and iteration < max_iterations:
                z = z * z + c
                iteration += 1

            # Map the iteration count to an ASCII character index
            # More iterations (inside Mandelbrot set) mapped to first characters of 'chars'
            char_idx = int((iteration / max_iterations) * (len(chars) - 1))
            row_output.append(chars[char_idx])

        # Print the finished row
        print("".join(row_output))


def generate_sierpinski(size):
    """
    Generates and prints a Sierpinski Triangle in ASCII art using bitwise AND operations.
    The Sierpinski triangle can be generated using Pascal's triangle modulo 2,
    which corresponds to the bitwise AND of row and column coordinates.
    """
    # Loop through each row of the triangle
    for y in range(size):
        # Print leading spaces to center/align the triangle nicely
        print(" " * (size - y - 1), end="")

        # Loop through each position in the row
        for x in range(y + 1):
            # Bitwise AND determines if a character should be printed or left empty
            # If the bitwise AND is zero, it forms part of the Sierpinski triangle
            if (x & (y - x)) == 0:
                # Print an asterisk followed by a space to maintain visual proportions
                print("* ", end="")
            else:
                print("  ", end="")
        print()


def main():
    print("=== ASCII Fractal Creator ===")
    print("Choose a fractal type to generate:")
    print("1. Mandelbrot Set (ASCII Art)")
    print("2. Sierpinski Triangle (ASCII Art)")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        print("\n--- Mandelbrot Set Parameters ---")
        try:
            # Get user inputs for size and complexity with reasonable defaults
            width = input("Enter terminal width for display (default: 80): ").strip()
            width = int(width) if width else 80

            height = input("Enter terminal height for display (default: 40): ").strip()
            height = int(height) if height else 40

            max_iterations = input("Enter max iterations (default: 30, higher means more detail): ").strip()
            max_iterations = int(max_iterations) if max_iterations else 30

            if width <= 0 or height <= 0 or max_iterations <= 0:
                print("All parameters must be positive integers.")
                return

            print("\nGenerating Mandelbrot Set...\n")
            generate_mandelbrot(width, height, max_iterations)

        except ValueError:
            print("Invalid input. Please enter integers.")

    elif choice == "2":
        print("\n--- Sierpinski Triangle Parameters ---")
        try:
            # Size must be a power of 2 for a perfectly aligned triangle (e.g., 16, 32, 64)
            size_input = input("Enter height/size of the triangle (best with powers of 2 like 16, 32, default: 32): ").strip()
            size = int(size_input) if size_input else 32

            if size <= 0:
                print("Size must be a positive integer.")
                return

            print("\nGenerating Sierpinski Triangle...\n")
            generate_sierpinski(size)

        except ValueError:
            print("Invalid input. Please enter an integer.")

    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
