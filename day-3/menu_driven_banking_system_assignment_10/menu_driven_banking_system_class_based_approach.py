'''
10. Menu-Driven Banking System 
Use dictionaries and functions. 
Support: 
1. Create account 
2. Deposit 
3. Withdraw 
4. Check balance 
5. Transfer 
6. Exit 
Example account: 
{ 
} 
"account_number": "ACC1001", 
"name": "Poku", 
"balance": 5000 
Create functions: 
create_account() 
deposit() 
withdraw() 
transfer() 
get_balance() 
Handle 
● Invalid account 
● Negative amount 
● Insufficient balance 
● Duplicate account number
'''

'''
class based Approach
'''

class InvalidAccountError(Exception):
    pass

class NegativeAmountError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class DuplicateAccountError(Exception):
    pass

class Bank:
    def __init__(self):
        self.accounts = {
            "ACC1001": {
                "account_number": "ACC1001",
                "name": "Poku",
                "balance": 5000
            }
        }

    def create_account(self,account_number,name,balance):
        if account_number in self.accounts:
            raise DuplicateAccountError("Account number already exists.")

        if balance < 0:
            raise NegativeAmountError("Initial balance cannot be negative.")

        self.accounts[account_number] = {
            "account_number": account_number,
            "name": name,
            "balance": balance
        }

        print("Account created successfully.")

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            raise InvalidAccountError("Invalid account number.")

        if amount <= 0:
            raise NegativeAmountError("Deposit amount must be positive.")

        self.accounts[account_number]["balance"] += amount
        print("Deposit successful.")

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            raise InvalidAccountError("Invalid account number.")

        if amount <= 0:
            raise NegativeAmountError("Withdrawal amount must be positive.")

        if amount > self.accounts[account_number]["balance"]:
            raise InsufficientBalanceError("Insufficient balance.")

        self.accounts[account_number]["balance"] -= amount
        print("Withdrawal successful.")

    def get_balance(self, account_number):
        if account_number not in self.accounts:
            raise InvalidAccountError("Invalid account number.")

        balance = self.accounts[account_number]["balance"]
        print("Current balance:", balance)
        return balance

    def transfer(self,from_account,to_account,amount):
        if from_account not in self.accounts:
            raise InvalidAccountError("Sender account does not exist.")

        if to_account not in self.accounts:
            raise InvalidAccountError("Receiver account does not exist.")

        if amount <= 0:
            raise NegativeAmountError("Transfer amount must be positive.")

        if amount > self.accounts[from_account]["balance"]:
            raise InsufficientBalanceError("Insufficient balance.")

        self.accounts[from_account]["balance"] -= amount
        self.accounts[to_account]["balance"] += amount
        print("Transfer successful.")


bank = Bank()

while True:
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Transfer")
    print("6. Exit")
    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            account_number = input("Enter account number: ")
            name = input("Enter name: ")
            balance = float(input("Enter initial balance: "))
            bank.create_account(account_number,name,balance)
        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number,amount)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number,amount)
        elif choice == "4":
            account_number = input("Enter account number: ")
            bank.get_balance(account_number)
        elif choice == "5":
            from_account = input("Enter sender account: ")
            to_account = input("Enter receiver account: ")
            amount = float(input("Enter transfer amount: "))
            bank.transfer(from_account,to_account,amount)
        elif choice == "6":
            print("Thank you for using the banking system.")
            break
        else:
            print("Invalid choice.")
    except (
        InvalidAccountError,
        NegativeAmountError,
        InsufficientBalanceError,
        DuplicateAccountError
    ) as error:
        print("Error:", error)
    except ValueError:
        print("Please enter a valid number.")
