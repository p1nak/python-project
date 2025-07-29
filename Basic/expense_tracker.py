import os 
import json
from datetime import datetime

FILENAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME , "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

def save_expenses(expenses):
    with open(FILENAME , "w") as f:
        json.dump(expenses , f , indent = 4)

def add_expenses(expenses):
    try:
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category (e.g. Food, Travel, Shopping): ").strip()
        description = input("Enter description: ").strip()
        date = datetime.now().strftime("%Y-%m-%d")

        expenses.append({
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        })
        print("Expenses added....")
    except ValueError:
        print("Invalid input. amount is always in number!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n📋 Your Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['description']} | {exp['date']}")

def show_summary(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total spent: ₹{total:.2f}")

def main():
    expenses = load_expenses()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Save and Exit")

        choice = input("👉 Choose an option (1-4): ").strip()

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            save_expenses(expenses)
            print("💾 Saved! Exiting...")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
