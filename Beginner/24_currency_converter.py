# Fixed exchange rates (relative to USD)
# In a real application, you would get this data from an API
RATES = {
    "USD": 1.0,
    "EUR": 0.94,
    "GBP": 0.82,
    "JPY": 149.85,
    "AUD": 1.56,
}

print("Available currencies: USD, EUR, GBP, JPY, AUD")

# Get user input
from_currency = input("Enter the currency to convert from: ").upper()
to_currency = input("Enter the currency to convert to: ").upper()
amount = float(input("Enter the amount to convert: "))

# Check if currencies are valid
if from_currency not in RATES or to_currency not in RATES:
    print("Invalid currency. Please choose from the available currencies.")
else:
    # Perform conversion
    # First, convert the amount to USD (the base currency)
    amount_in_usd = amount / RATES[from_currency]
    # Then, convert from USD to the target currency
    converted_amount = amount_in_usd * RATES[to_currency]

    # Display the result
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
