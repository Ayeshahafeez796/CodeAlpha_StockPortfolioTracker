# Stock Portfolio Tracker — CodeAlpha Internship Task
# Author: Ayesha hafeez
# Features: Dictionary, Arithmetic, File Handling, Input/Output

import json

PORTFOLIO_FILE = "portfolio.json"

def get_stock_data():
    """Input stock info and return as dictionary"""
    name = input("Enter stock name: ")
    while True:
        try:
            shares = int(input("Enter number of shares: "))
            price = float(input("Enter price per share: "))
            break
        except ValueError:
            print("Please enter valid numbers!")
    
    total_value = shares * price
    return {
        "name": name,
        "shares": shares,
        "price": price,
        "total": total_value
    }

def save_portfolio(portfolio):
    """Save portfolio to JSON file"""
    with open(PORTFOLIO_FILE, "w") as f:
        json.dump(portfolio, f, indent=4)

def load_portfolio():
    """Load portfolio from JSON file if exists"""
    try:
        with open(PORTFOLIO_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def main():
    print("\n===== STOCK PORTFOLIO TRACKER =====\n")

    portfolio = load_portfolio()
    if portfolio:
        print("Existing portfolio loaded from file.\n")

    stock_count = int(input("How many stocks do you want to add? "))

    for _ in range(stock_count):
        print("\n--- Add New Stock ---")
        stock = get_stock_data()
        portfolio.append(stock)

    save_portfolio(portfolio)

    grand_total = sum(stock["total"] for stock in portfolio)

    print("\n===== PORTFOLIO SUMMARY =====")
    for stock in portfolio:
        print(
            f"{stock['name']} — {stock['shares']} × {stock['price']} = {stock['total']}"
        )

    print(f"\nTotal Investment: {grand_total}")
    print("\nPortfolio saved to portfolio.json. Thank you for using the tracker!")

if __name__ == "__main__":
    main()
