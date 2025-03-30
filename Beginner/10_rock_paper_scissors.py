import random

options = ["rock", "paper", "scissors"]

# Allow for replays using a while loop
while True:
    # Get the user's choice
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    # Validation
    if user_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Choose a random computer choice
    computer_choice = random.choice(options)
    print(f"Computer chose {computer_choice}.")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

    # Ask if the user wants to play again
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break