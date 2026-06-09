import csv
FILE_NAME = "expenses.csv"

def add_expense():
    date = input("Enter the date of the expense (DD-MM-YYYY): ")
    category = input("Enter the category of the expense (Travel, Food, etc.): ")
    amount = float(input("Enter the amount of the expenses: "))


    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("Expense added successfully!")

def view_expenses():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            print("\nExpenses:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found. Please add an expense first.")

while True:   
    print("\n---Smart Expense Tracer---")   
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit") 

    choice = input("Enter your choice: ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:        
        print("Invalid choice. Please try again.")
