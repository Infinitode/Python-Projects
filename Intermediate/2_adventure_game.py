import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def get_choice(choices):
    while True:
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice}")
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def intro():
    print_slow("You wake up in a dark, cold room.")
    print_slow("You see a door in front of you.")
    print_slow("What do you do?")
    choice = get_choice(["Open the door", "Look for a light switch"])
    if choice == 1:
        open_door()
    else:
        light_switch()

def open_door():
    print_slow("The door is locked.")
    print_slow("You need a key.")
    intro()

def light_switch():
    print_slow("You find a light switch and flick it on.")
    print_slow("The room is empty except for a small key on the floor.")
    print_slow("What do you do?")
    choice = get_choice(["Pick up the key", "Go back to the door"])
    if choice == 1:
        pick_up_key()
    else:
        open_door()

def pick_up_key():
    print_slow("You pick up the key.")
    print_slow("You go back to the door and unlock it.")
    print_slow("You have escaped the room!")
    print_slow("Congratulations!")

def main():
    intro()

if __name__ == "__main__":
    main()
