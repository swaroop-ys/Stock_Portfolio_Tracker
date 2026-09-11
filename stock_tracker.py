# CodeAlpha Python Programming Internship
# Task 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 350,
    "AMZN": 170
}

portfolio = {}
total_investment = 0

print("=" * 50)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 50)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

print("\nEnter your stock details.")
print("Type 'DONE' when you finish.\n")

while True:
    stock_name = input("Enter stock symbol: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the list.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f"Added {quantity} shares of {stock_name}")

    except ValueError:
        print("Please enter a valid number.")

print("\n" + "=" * 50)
print("           PORTFOLIO SUMMARY")
print("=" * 50)

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value

    print(f"\nStock: {stock}")
    print(f"Quantity: {quantity}")
    print(f"Price per Share: ${price}")
    print(f"Total Value: ${value}")

print("\n" + "-" * 50)
print(f"TOTAL INVESTMENT VALUE: ${total_investment}")
print("-" * 50)

with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("=" * 40 + "\n\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity

        file.write(f"Stock: {stock}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Price per Share: ${price}\n")
        file.write(f"Total Value: ${value}\n\n")

    file.write("-" * 40 + "\n")
    file.write(f"TOTAL INVESTMENT VALUE: ${total_investment}\n")

print("\nPortfolio saved successfully to portfolio.txt")
print("Thank you for using Stock Portfolio Tracker!")
