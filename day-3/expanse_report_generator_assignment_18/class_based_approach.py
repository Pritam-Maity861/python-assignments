class ExpenseReport:
    def __init__(self, expenses):
        self.expenses = expenses

    def calculate_total(self):
        if not self.expenses:
            raise ValueError("Expenses cannot be empty.")
        total = 0
        for expense in self.expenses:
            amount = expense["amount"]

            if not isinstance(amount, (int, float)) or amount < 0:
                raise ValueError("Expense amount must be a valid positive number.")
            total += amount

        return total

    def group_by_category(self):
        if not self.expenses:
            raise ValueError("Expenses cannot be empty.")
        categories = {}
        for expense in self.expenses:
            amount = expense["amount"]

            if not isinstance(amount, (int, float)) or amount < 0:
                raise ValueError("Expense amount must be a valid positive number.")

            category = expense["category"]

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

        return categories

    def get_highest_category(self):
        categories = self.group_by_category()
        return max(categories, key=categories.get)

    def generate_report(self):
        total = self.calculate_total()
        categories = self.group_by_category()
        highest_category = self.get_highest_category()
        print("Total Expense: ₹", total)
        print()
        for category, amount in categories.items():
            print(f"{category}: ₹{amount}")

        print()
        print("Highest Category:", highest_category)


expenses = [
    {"category": "Food", "amount": 500},
    {"category": "Travel", "amount": 1000},
    {"category": "Food", "amount": 300},
    {"category": "Shopping", "amount": 2000}
]

try:
    report = ExpenseReport(expenses)
    report.generate_report()
except ValueError as error:
    print("Error:", error)
