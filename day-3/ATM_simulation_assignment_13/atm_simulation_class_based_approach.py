class InvalidPINError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class ATM:
    def __init__(self):
        self.pin = "1234"
        self.balance = 5000

    def validate_pin(self, user_pin):
        if len(user_pin) != 4 or not user_pin.isdigit():
            raise InvalidPINError("PIN must be exactly 4 digits.")

    def check_balance(self):
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")

        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance.")

        self.balance -= amount
        print("Withdrawal successful.")
        print("Remaining balance:", self.balance)

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")

        self.balance += amount
        print("Deposit successful.")
        print("Current balance:", self.balance)

    def change_pin(self, new_pin):
        self.validate_pin(new_pin)
        self.pin = new_pin
        print("PIN changed successfully.")


atm = ATM()

attempts = 0
login_success = False

while attempts < 3:
    user_pin = input("Enter PIN: ")
    try:
        atm.validate_pin(user_pin)
        if user_pin == atm.pin:
            login_success = True
            print("Login successful.")
            break
        else:
            attempts += 1
            print("Incorrect PIN.")
    except InvalidPINError as error:
        attempts += 1
        print("Error:", error)

if not login_success:
    print("Maximum attempts exceeded. Card blocked.")
else:
    while True:
        print("\n1. Check balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change PIN")
        print("5. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                atm.check_balance()
            elif choice == "2":
                amount = float(input("Enter amount: "))
                atm.withdraw(amount)
            elif choice == "3":
                amount = float(input("Enter amount: "))
                atm.deposit(amount)
            elif choice == "4":
                new_pin = input("Enter new PIN: ")
                atm.change_pin(new_pin)
            elif choice == "5":
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid choice.")
        except (InvalidAmountError, InsufficientBalanceError, InvalidPINError) as error:
            print("Error:", error)
        except ValueError:
            print("Please enter a valid amount.")
