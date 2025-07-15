# Python Projects

An open-source GitHub repository containing Python project ideas, steps, tips, and code solutions.

This repository is designed to help Python learners at all levels, starting with beginner-friendly projects and gradually progressing to more advanced ones. Each project includes clear instructions and a working code implementation.

## Table of Contents
1. [Setup](#setup)
2. [Beginner Projects](#beginner-projects)
3. [Intermediate Projects](#intermediate-projects)
4. [Contributing](#contributing)
5. [License](#license)

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

### 6. Palindrome Checker
- **Description**: Build a simple palindrome checker.

- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Beginner/6_palindrome_checker.py

- **Steps**:
  1. Prompt the user for a word.
  2. Reverse the string.
  3. Check if it is equal to the original.
  4. Display the result.

- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use `input()` for input.

    </details>
    <details><summary>Tip 2:</summary>

    You can easily reverse the string using array manipulation techniques. `[::-1]`

    </details>
    <details><summary>Tip 3:</summary>

    Print out the result using `print()`.

    </details>

### 7. Word Counter
- **Description**: Build a simple word counter.

- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Beginner/7_word_counter.py

- **Steps**:
  1. Prompt the user for a file path (TXT).
  2. Read the file path.
  3. Count the words in the read data.
  4. Display the result.

- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use `input()` for input.

    </details>
    <details><summary>Tip 2:</summary>

    Read the file using `read operations` (https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/) in Python.

    </details>
    <details><summary>Tip 3:</summary>

    Count the number of words using `split()` and `len()`.

    </details>
    <details><summary>Tip 4:</summary>

    Print out the result using `print()`.

    </details>

### 8. Text Encryption
- **Description**: Create a text encryption function with decryption as well.

- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Beginner/8_text_encryption.py

- **Steps**:
  1. Prompt the user for text and a password (to be used for encryption).
  2. Encrypt the text.
  3. Decrypt the text.
  4. Display the results.

- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use `input()` for input.

    </details>
    <details><summary>Tip 2:</summary>

    Use simple encryption methods like Caesar cipher.

    </details>
    <details><summary>Tip 3:</summary>

    Store the password in a variable to use it later during decryption.

    </details>
    <details><summary>Tip 4:</summary>

    Print out the results using `print()`.

    </details>

### 9. Countdown Timer
- **Description**: Create a countdown timer for seconds and minutes.

- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Beginner/9_countdown_timer.py

- **Steps**:
  1. Prompt the user for a time, in a specific format.
  2. Extract information from the provided time.
  3. Countdown.
  4. Display the results.

- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use `input()` for input.

    </details>
    <details><summary>Tip 2:</summary>

    Use simple string manipulation techniques to get the minutes and seconds from the provided time.

    </details>
    <details><summary>Tip 3:</summary>

    Use `time.sleep(1)` to count down in seconds.

    </details>
    <details><summary>Tip 4:</summary>

    Print out the results using `print()`.

    </details>

### 10. Rock Paper Scissors
- **Description**: Create a rock paper scissors game.

- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Beginner/10_rock_paper_scissors.py

- **Steps**:
  1. Prompt the user for a choice.
  2. Generate a random choice for the computer.
  3. Compare the choices.
  4. Display the results.

- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use `input()` for input.

    </details>
    <details><summary>Tip 2:</summary>

    Use `random.choice()` to generate a random choice for the computer.

    </details>
    <details><summary>Tip 3:</summary>

    Use `conditional` statements to compare the choices and determine the winner.

    </details>
    <details><summary>Tip 4:</summary>

    Print out the results using `print()`.

    </details>

### 11. Mad Libs Generator
- **Description**: Create a Mad Libs generator.

- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Beginner/11_mad_libs_generator.py

- **Steps**:
  1. Define a template for the Mad Libs story.
  2. Prompt the user for different types of words (noun, verb, adjective, etc.).
  3. Replace the placeholders in the template with the user's words.
  4. Display the completed Mad Libs story.

- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use `input()` for input.

    </details>
    <details><summary>Tip 2:</summary>

    Use string formatting to replace the placeholders in the template.

    </details>
    <details><summary>Tip 3:</summary>

    Create multiple templates for different stories.

    </details>
    <details><summary>Tip 4:</summary>

    Print out the results using `print()`.

    </details>

### 12. Dice Rolling Simulator
- **Description**: Create a dice rolling simulator.

- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Beginner/12_dice_rolling_simulator.py

- **Steps**:
  1. Prompt the user for the number of dice to roll.
  2. Roll the dice.
  3. Display the results.

- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use `input()` for input.

    </details>
    <details><summary>Tip 2:</summary>

    Use `random.randint()` to generate a random number between 1 and 6.

    </details>
    <details><summary>Tip 3:</summary>

    Use a `loop` to roll multiple dice.

    </details>
    <details><summary>Tip 4:</summary>

    Print out the results using `print()`.

    </details>

> [!NOTE]
> Working code solutions are in the `/Beginner` folder.

### 13. Hangman Game
- **Description**: Implement the classic Hangman game where the player guesses letters to reveal a hidden word.
- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Beginner/13_hangman_game.py
- **Steps**:
  1. Create a list of words for the game.
  2. Randomly select a word.
  3. Display the word with blanks for hidden letters.
  4. Allow the user to guess letters.
  5. Keep track of guessed letters and remaining attempts.
  6. Reveal letters in the word as they are guessed correctly.
  7. End the game when the word is guessed or attempts run out.
- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use `random.choice()` to select a random word from a list.

    </details>
    <details><summary>Tip 2:</summary>

    Use a `while` loop for the main game interactions.

    </details>
    <details><summary>Tip 3:</summary>

    Store guessed letters in a list to avoid repeat guesses and display them to the user.

    </details>
    <details><summary>Tip 4:</summary>

    Represent the hidden word as a list of characters or underscores, updating it as letters are guessed.

    </details>
    <details><summary>Tip 5:</summary>

    Keep a counter for incorrect guesses (attempts remaining).

    </details>

### 14. Address Book
- **Description**: A simple command-line contact manager.
- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Beginner/14_address_book.py
- **Steps**:
  1. Create functions to add, view, and delete contacts.
  2. Store contacts in a file (e.g., JSON).
  3. Create a main loop to interact with the user.
- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use a dictionary to store contact information.

    </details>
    <details><summary>Tip 2:</summary>

    Use the `json` module to save and load contacts from a file.

    </details>

### 15. Pomodoro Timer
- **Description**: A time management tool to help you stay focused.
- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Beginner/15_pomodoro_timer.py
- **Steps**:
  1. Create a function to run a countdown timer.
  2. Prompt the user for work and break durations.
  3. Alternate between work and break sessions.
- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use the `time` module to pause execution.

    </details>
    <details><summary>Tip 2:</summary>

    Use a loop to alternate between work and break sessions.

    </details>

### 16. Budget Tracker
- **Description**: A tool to track your income and expenses.
- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Beginner/16_budget_tracker.py
- **Steps**:
  1. Create functions to add income and expenses.
  2. Store transactions in a file (e.g., JSON).
  3. Calculate and display the current balance.
- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use lists of dictionaries to store income and expense transactions.

    </details>
    <details><summary>Tip 2:</summary>

    Use the `json` module to save and load transaction data.

    </details>

## Intermediate Projects
These projects are ideal for those with experience in Python. Each project includes a description, steps to follow, and tips for completing it.

### 1. Tic Tac Toe
- **Description**: Build a tic tac toe board, with it's own algorithm for winning and countering player moves.

- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Intermediate/1_tic_tac_toe.py

- **Steps**:
  1. Create the board (3x3 grid) and other logic (handling invalid moves, etc.)
  2. Handle player and computer moves, including ties, wins and losses.
  3. Display the board and start the game.

- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use functions for repetitive tasks.

    </details>
    <details><summary>Tip 2:</summary>

    Create an algorithm that not only chooses certain priority positions on the board, but also counters player moves.

    </details>
    <details><summary>Tip 3:</summary>

    Add error handling and retries if a player chooses a place on the board that is already occupied.

    </details>

> [!NOTE]
> Working code solutions are in the `/Intermediate` folder.

### 2. Text-based Adventure Game
- **Description**: An interactive fiction game where you can explore and make choices.
- **Solution**: https://github.com/Infinitode/Python-Projects/blob/main/Intermediate/2_adventure_game.py
- **Steps**:
  1. Create a story with different rooms and choices.
  2. Use functions to represent different parts of the story.
  3. Get user input to navigate through the story.
- **Tips:**

    </summary>
    <details><summary>Tip 1:</summary>

    Use a dictionary to define the game world, with rooms, descriptions, and choices.

    </details>
    <details><summary>Tip 2:</summary>

    Use a loop to keep the game running until the player reaches an end state.

    </details>

## Contributing
Contributions are welcome! If you have project ideas or improvements, feel free to fork the repository and open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
