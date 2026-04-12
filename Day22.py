# Expense Tracker Application

expenses = []

# Load data from file
def load_expenses():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                amount, category, date = line.strip().split(",")
                expenses.append({
                    "amount": float(amount),
                    "category": category,
                    "date": date
                })
    except FileNotFoundError:
        pass


# Save data to file
def save_expenses():
    with open("expenses.txt", "w") as file:
        for exp in expenses:
            file.write(f"{exp['amount']},{exp['category']},{exp['date']}\n")


# Add expense
def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food/Travel/etc): ")
        date = input("Enter date (DD-MM-YYYY): ")

        expenses.append({
            "amount": amount,
            "category": category,
            "date": date
        })

        print("Expense added successfully!")

    except ValueError:
        print("Invalid input! Please enter correct amount.")


# View expenses
def view_expenses():
    if not expenses:
        print("No expenses found.")
    else:
        print("\n--- All Expenses ---")
        for i, exp in enumerate(expenses, start=1):
            print(i, exp)


# Delete expense
def delete_expense():
    view_expenses()
    if expenses:
        try:
            num = int(input("Enter expense number to delete: "))
            if 1 <= num <= len(expenses):
                removed = expenses.pop(num - 1)
                print("Deleted:", removed)
            else:
                print("Invalid number!")
        except ValueError:
            print("Enter valid number!")


# Total expense
def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print("Total Expense:", total)


# Category-wise expense
def category_expense():
    summary = {}
    for exp in expenses:
        cat = exp["category"]
        summary[cat] = summary.get(cat, 0) + exp["amount"]

    print("\n--- Category Wise Expense ---")
    for cat, amt in summary.items():
        print(cat, ":", amt)


# Main program
def main():
    load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Total Expense")
        print("5. Category Wise Expense")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            total_expense()
        elif choice == "5":
            category_expense()
        elif choice == "6":
            save_expenses()
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice!")


# Run program
if __name__ == "__main__":
    main()
