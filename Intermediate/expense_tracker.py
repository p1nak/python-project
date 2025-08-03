import os
import json
from datetime import datetime
from collections import defaultdict

FILENAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    return []

def save_expenses(expenses):
    with open(FILENAME, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses): 
    try:
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category (e.g. Food, Travel, Shopping): ").strip().title() 
        description = input("Enter description: ").strip()
        date = input(f"Enter date (YYYY-MM-DD) [Today: {datetime.now().strftime('%Y-%m-%d')}]: ").strip()
        
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        else:
            datetime.strptime(date, "%Y-%m-%d") 

        expenses.append({
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        })
        print("✅ Expense added successfully!")  
    except ValueError as e:
        print(f"❌ Error: {str(e)}")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n📋 Your Expenses:")
    print(f"{'No.':<4} {'Amount':<10} {'Category':<15} {'Date':<12} Description")
    print("-" * 60)
    for i, exp in enumerate(expenses, 1):
        print(f"{i:<4} ₹{exp['amount']:<9.2f} {exp['category']:<15} {exp['date']:<12} {exp['description']}")

def show_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return
    
    category_totals = defaultdict(float)
    for exp in expenses:
        category_totals[exp['category']] += exp['amount']
    
    total = sum(category_totals.values())
    
    print("\n💰 Spending Summary:")
    for category, amount in sorted(category_totals.items()):
        print(f"  {category:<15}: ₹{amount:.2f} ({amount/total:.1%})")
    print("-" * 30)
    print(f"  {'Total':<15}: ₹{total:.2f}")

def filter_expenses(expenses):
    print("\n🔍 Filter Options:")
    print("1. By Category")
    print("2. By Date Range")
    print("3. Cancel")
    
    choice = input("Choose filter option (1-3): ").strip()
    
    if choice == "1":
        category = input("Enter category name: ").strip().title()
        filtered = [exp for exp in expenses if exp['category'].title() == category]
        if not filtered:
            print(f"No expenses found in category '{category}'")
        else:
            view_expenses(filtered)
    elif choice == "2":
        try:
            start_date = input("Enter start date (YYYY-MM-DD): ").strip()
            end_date = input("Enter end date (YYYY-MM-DD): ").strip()
            
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")
            
            filtered = [
                exp for exp in expenses
                if start_date <= exp['date'] <= end_date
            ]
            view_expenses(filtered)
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")
    elif choice == "3":
        return
    else:
        print("Invalid choice")

def main():
    expenses = load_expenses()
    
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Spending Summary")
        print("4. Filter Expenses")
        print("5. Save and Exit")
        
        choice = input("👉 Choose an option (1-5): ").strip()
        
        if choice == "1":
            add_expense(expenses)  
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            filter_expenses(expenses)
        elif choice == "5":
            save_expenses(expenses)
            print("💾 Expenses saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
