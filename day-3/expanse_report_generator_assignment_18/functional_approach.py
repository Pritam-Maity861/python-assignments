expenses = [
    {"category": "Food", "amount": 500},
    {"category": "Travel", "amount": 1000},
    {"category": "Food", "amount": 300},
    {"category": "Shopping", "amount": 2000}
]


def calculate_total(expenses):
    if not expenses:
        raise ValueError("Expenses cannot be empty.")

    total = 0
    for expense in expenses:
        amount = expense["amount"]
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Expense amount must be a valid positive number.")
        total += amount

    return total


def group_by_category(expenses):
    if not expenses:
        raise ValueError("Expenses cannot be empty.")
    categories = {}
    for expense in expenses:
        amount = expense["amount"]
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Expense amount must be a valid positive number.")

        category = expense["category"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    return categories


def get_highest_category(expenses):
    categories = group_by_category(expenses)

    return max(categories, key=categories.get)


def generate_report(expenses):
    total = calculate_total(expenses)
    categories = group_by_category(expenses)
    highest_category = get_highest_category(expenses)

    print("Total Expense: ₹", total)
    print()
    for category, amount in categories.items():
        print(f"{category}: ₹{amount}")

    print()
    print("Highest Category:", highest_category)


try:
    generate_report(expenses)
except ValueError as error:
    print("Error:", error)
