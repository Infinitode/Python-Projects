# 7. Bank Account Simulator (OOP)

import uuid


class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        self.account_id = str(uuid.uuid4())[:8]

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def __str__(self):
        return f"Account Owner: {self.owner}\nAccount ID: {self.account_id}\nBalance: ${self.balance:.2f}"


def main():
    print("=== Bank Account Simulator ===")
    owner_name = input("Enter account owner name: ")
    initial_balance = float(input("Enter initial balance: "))

    my_account = Account(owner_name, initial_balance)

    while True:
        print("\n=== Account Menu ===")
        print("1. Account Overview")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            print(my_account)
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            my_account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            my_account.withdraw(amount)
        elif choice == '4':
            print("Thank you for using our bank services!")
            break
        else:
            print("Invalid Selection.")


if __name__ == "__main__":
    main()
