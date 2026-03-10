import json
from pathlib import Path
import datetime

transaction = []
finance = Path("finance.json")

def laod_data(finance):

    if not finance.exists():
        return []
    try:
        with open(finance, 'r') as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError:
        return []

def add_income(transaction):
    while True:
        try:
            income = float(input("Enter Income Amount: "))
            break
        except ValueError:
            print("Enter Number.")
    category = input("Enter Category: ").capitalize()

    transaction.append({
        "Type" : "Income",
        "Income Amount" : income,
        "Category" : category,
        "Date" : str(datetime.date.today().strftime("%Y-%m-%d"))
    })

def add_expenses(transaction):
    while True:
        try:
            expense = float(input("Enter Expense Amount: "))
            break
        except ValueError:
            print("Enter Number.")
    category = input("Enter Category: ").capitalize()

    transaction.append({
        "Type" : "Expense",
        "Expense Amount" : expense,
        "Category" : category,
        "Date" : str(datetime.date.today().strftime("%Y-%m-%d"))
    })

def save_data(transaction):

    with open(finance, 'w') as f:
        json.dump(transaction, f, indent=4)

def show_total_balance(transaction):

    if not transaction:
        print("There is nothing to Show.")

    total_income = 0
    total_expenses = 0

    for i in transaction:
        if i["Type"] == "Income":
            total_income += i["Income Amount"]

        elif i["Type"] == "Expense":
            total_expenses +=  i["Expense Amount"]

    total_balance = total_income - total_expenses

    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print()
    print(f"Total Income: {total_income} ")
    print(f"Total Expenses: {total_expenses}")
    print(f"Total Balance: {total_balance}")
    print()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def show_monthly_summary(transaction):

    user_month = input("Enter month (YYYY-MM): ").strip()

    total_income = 0
    total_expenses = 0

    for t in transaction:
        if t["Date"].startswith(user_month):

            if t["Type"] == "Income":
                total_income += t["Income Amount"]

            elif t["Type"] == "Expense":
                total_expenses +=  t["Expense Amount"]
        else:
            print("There is no Date for this Month!.")

    total_balance = total_income - total_expenses
    print("=======================================")
    print()
    print(f"Total Income: {total_income} ")
    print(f"Total Expenses: {total_expenses}")
    print(f"Total Balance: {total_balance}")
    print()
    print("=======================================")

def main():
    transaction = laod_data(finance)

    while True:
        print("------------------------------")
        print()
        print("1: Add Income")
        print("2: Add Expenses")
        print("3: Show Total Balance")
        print("4: Show monthly Summary")
        print("5: Exit")
        print()
        print("------------------------------")

        try:
            user = int(input("Enter Number(1-5): "))
            if user == 1:
                add_income(transaction)
                save_data(transaction)
            elif user == 2:
                add_expenses(transaction)
                save_data(transaction)
            elif user == 3:
                show_total_balance(transaction)
            elif user == 4:
                show_monthly_summary(transaction)
            else:
                print("GoodBye!")
                break
        except ValueError:
            print("Eneter Number.")


main()