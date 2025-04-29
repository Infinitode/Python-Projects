import random

def roll_dice(num_dice):
    """
    Simulates rolling a specified number of standard 6-sided dice.

    Args:
        num_dice (int): The number of dice to roll.

    Returns:
        tuple: A tuple containing:
            - list: A list of the individual dice roll results.
            - int: The sum of all dice rolls.
    """
    rolls = []
    total_sum = 0
    for _ in range(num_dice):
        # Roll a single 6-sided die
        roll = random.randint(1, 6)
        rolls.append(roll)
        total_sum += roll
    return rolls, total_sum

def main():
    """
    Main function to run the dice rolling simulator.
    """
    print("--- Dice Rolling Simulator ---")

    while True:
        try:
            # 1. Prompt the user for the number of dice to roll
            num_dice_str = input("How many dice do you want to roll? ")
            num_dice = int(num_dice_str)

            if num_dice <= 0:
                print("Please enter a positive number of dice.")
                continue # Ask again

            # 2. Roll the dice
            individual_rolls, total = roll_dice(num_dice)

            # 3. Display the results
            print(f"\nRolling {num_dice} dice...")
            print(f"Individual rolls: {individual_rolls}")
            print(f"Total sum: {total}")
            break # Exit the loop after successful roll

        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break # Exit on other errors

if __name__ == "__main__":
    main()