#classes and objects
class Dog:
    def __init__(self, name, breed):  # Constructor method
        self.name = name  # Attribute
        self.breed = breed

my_dog = Dog("Buddy", "Golden Retriever")  # Creating an object
print(my_dog.name)  # Output: Buddy





#Attributes and methods
class Dog:
   
    def __init__(self, name, breed):
        self.name = name  #attribute
        self.breed = breed

    def bark(self):  # Method
        return "Woof!"

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())  # Output: Woof!





#Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def get_balance(self):  # Controlled access
        return self.__balance

account = BankAccount(1000)
print(account.get_balance())  # Output: 1000
print(account.get_balance())  # Error! Can't access directly





#Inheritance
class Animal:
    def speak(self):
        return "I make a noise."

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return "Woof!"

my_dog = Dog()
print(my_dog.speak())  # Output: Woof!





#Polymorphism 
class Cat:
    def speak(self):
        return "Meow!"

class Dog:
    def speak(self):
        return "Woof!"

animals = [Cat(), Dog()]
for animal in animals:
    print(animal.speak())  # Output: Meow! Woof!