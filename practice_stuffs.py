class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        print(f"Account created for {self.account_holder} with initial balance ${self.balance}.")
def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                print(f"Deposited ${amount}. New balance is ${self.balance}.")
            else:
                print("Deposit amount must be positive.")
def withdraw(self, amount):
            if amount <= 0:
                print("Withdrawal amount must be positive.")
            elif amount > self.balance:
                print(f"You don't have enough balance for this withdrawal.Unless you want to have less than no money, Imagine you want ${amount} but you only have ${self.balance}!.")
            else:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance is ${self.balance}.")
def display_balance(self):
            print(f"{self.account_holder} has ${self.balance} in their account.")
account = BankAccount("Elizabeth", 1000)
account.deposit(500)
account.deposit(800)
#account.deposit(-1000)
#account.withdraw(-2000)
account.withdraw(3000)
account.display_balance()
