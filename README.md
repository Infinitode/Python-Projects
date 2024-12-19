# Python Projects

An open-source GitHub repository containing Python project ideas, steps, tips, and code solutions.

This repository is designed to help Python learners at all levels, starting with beginner-friendly projects and gradually progressing to more advanced ones. Each project includes clear instructions and a working code implementation.

## Table of Contents
1. [Setup](#setup)
2. [Beginner Projects](#beginner-projects)
3. [Contributing](#contributing)
4. [License](#license)

## Setup

- Ensure have at least Python `3.6` or later (we recommend `3.12` or later) installed on your computer. You can do a quick search and download it from a trusted provider for your platform.

- Ensure you have an IDE or a place where you can code and run the Python interpreter.
> [!TIP]
> We use Visual Studio Code. It's fast, efficient, and has many extensions and customizability options.

## Beginner Projects
These projects are ideal for those new to Python. Each project includes a description, steps to follow, and tips for completing it.

### 1. Calculator
- **Description**: Build a simple calculator that performs basic arithmetic operations (`+`, `-`, `*`, `/`).

- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Beginner/1_calculator.py

- **Steps**:
  1. Prompt the user for two numbers and an operator.
  2. Perform the chosen operation.
  3. Display the result.

- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use `input()` to get the user's input. Learn more from here: https://docs.python.org/3/library/functions.html#input

    </details>
    <details><summary>Tip 2:</summary>

    Use `variables` to store the user's input.

    </details>
    <details><summary>Tip 3:</summary>

    Use `conditional` statements to check for valid values, and perform certain operations. Learn more from here: https://www.w3schools.com/python/python_conditions.asp

    </details>
    <details><summary>Tip 4:</summary>

    Print out the result using `print()`. Learn more from here: https://docs.python.org/3/library/functions.html#print

    </details>

### 2. Number Guessing Game
- **Description**: Build a simple random number generator, where users have to submit their guesses as to what the number is. Accept a range within 10 of the random number. `[0 - 100]`

- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Beginner/2_random_guesser.py

- **Steps**:
  1. Generate a random number within the range `0 - 100`.
  2. Prompt the user for a number input.
  3. Compare the input to a valid range within 10 of the random number.
  4. Display the result.

- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use the `random` module to generate a random number within the range.

    </details>
    <details><summary>Tip 2:</summary>

    Use `input()` to prompt the user for input.

    </details>
    <details><summary>Tip 3:</summary>

    Use `conditional` statements to check for valid values within the range of `10`. Learn more from here: https://www.w3schools.com/python/python_conditions.asp

    </details>
    <details><summary>Tip 4:</summary>

    Print out the result using `print()`. Learn more from here: https://docs.python.org/3/library/functions.html#print

    </details>

### 3. Password Generator
- **Description**: Build a simple password generator than can generate custom length passwords, from 8 up to 128 characters. Use uppercase, lowercase, symbols, and numbers.

- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Beginner/3_password_generator.py

- **Steps**:
  1. Define your password generator's maps or strings.
  2. Prompt the user for a number `[8 - 128]` input.
  3. Generate the password.
  4. Display the result.

- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use the `string` module for character sets like punctuation, letters or special characters.

    </details>
    <details><summary>Tip 2:</summary>

    Use `input()` to prompt the user for input.

    </details>
    <details><summary>Tip 3:</summary>

    Use a `loop` to generate the password up until the given length.

    </details>
    <details><summary>Tip 4:</summary>

    Print out the result using `print()`.

    </details>

### 4. Tip Calculator
- **Description**: Build a simple tip calculator, that calculates the tip based on the total and the desired percentage with splits.

- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Beginner/4_tip_calculator.py

- **Steps**:
  1. Get the total from the user.
  2. Get the tip percentage from the user.
  3. Get the amount of people who should split the bill.
  3. Calculate the tip.
  4. Display the result.

- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Get all inputs using `input()`.

    </details>
    <details><summary>Tip 2:</summary>

    Calculate the `tip_amount`, `new_total` and `splits_per_person` using basic arithmetic and math.

    </details>
    <details><summary>Tip 3:</summary>

    Print out the result using `print()`.

    </details>

### 5. Temperature Converter
- **Description**: Build a simple temperature converter that converts between Celsius and Fahrenheit.

- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Beginner/5_temperature_converter.py

- **Steps**:
  1. Define conversion values for each conversion.
  2. Prompt the user for the unit to convert to, and from.
  3. Prompt the user for a temperature value.
  4. Convert.
  5. Display the result.

- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use predefined formulas for accurate conversion between units.

    </details>
    <details><summary>Tip 2:</summary>

    Use `input()` to prompt the user for input.

    </details>
    <details><summary>Tip 3:</summary>

    Print out the result using `print()`.

    </details>

> [!NOTE]
> Working code solutions are in the `/Beginner` folder.

## Contributing
Contributions are welcome! If you have project ideas or improvements, feel free to fork the repository and open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
