#assignment 1
class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def display_student(self):
        print(f"Student: {self.name}, Roll No: {self.roll_number}, Grade: {self.grade}")

    def is_passed(self):
        return "Passed!" if self.grade >= 50 else "Failed."

# Creating an instance
student1 = Student("Alice", 101, 75)
student1.display_student()
print(student1.is_passed())  # Output: Passed!

#assignment 2
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  # Instance variable
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This car is a {self.year} {self.brand} {self.model}.")

my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()  # Output: This car is a 2020 Toyota Corolla.

#assignment 3
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

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