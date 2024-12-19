total = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15, etc.? ")
people = input("How many people to split the bill? ")

try:
    total = float(total)
    tip = int(tip)
    people = int(people)
    if tip < 0 or people < 1 or tip > 100 or total <= 0:
        raise ValueError

except ValueError:
    print("Please enter valid values.")
    exit()

tip_amount = total * (tip / 100)
total += tip_amount
tip_per_person = tip_amount / people
total_per_person = total / people

print(f"Your total is ${total:.2f} with tips.\nA tip amount of ${tip_amount:.2f}.\nSplit between {people} people.\nEach person should pay: ${total_per_person:.2f} or ${tip_per_person:.2f} for tips.")