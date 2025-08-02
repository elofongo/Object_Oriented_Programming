#assignment 3
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        print()


    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(f"{self.account_holder} has ${self.balance} in their account.")

# Example usage
account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
account.display_balance()