import json
import os

BUDGET_FILE = "budget.json"

def load_data():
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "r") as f:
            return json.load(f)
    return {"income": [], "expenses": []}

def save_data(data):
    with open(BUDGET_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_transaction(data, transaction_type):
    try:
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        data[transaction_type].append({"amount": amount, "description": description})
        save_data(data)
        print(f"{transaction_type.capitalize()} added.")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_transactions(data):
    print("\n--- Income ---")
    if not data["income"]:
        print("No income recorded.")
    else:
        for item in data["income"]:
            print(f"${item['amount']:.2f}: {item['description']}")

    print("\n--- Expenses ---")
    if not data["expenses"]:
        print("No expenses recorded.")
    else:
        for item in data["expenses"]:
            print(f"${item['amount']:.2f}: {item['description']}")

def calculate_balance(data):
    total_income = sum(item["amount"] for item in data["income"])
    total_expenses = sum(item["amount"] for item in data["expenses"])
    balance = total_income - total_expenses
    print(f"\nTotal Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")

def main():
    data = load_data()
    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction(data, "income")
        elif choice == "2":
            add_transaction(data, "expenses")
        elif choice == "3":
            view_transactions(data)
        elif choice == "4":
            calculate_balance(data)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
