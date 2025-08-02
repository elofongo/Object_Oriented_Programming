class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  # Instance variable
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This car is a {self.year}, {self.brand}, and {self.model}.")

    def plate_number(self):
        print(f"the plate number is {self.model}{self.year}{self.brand}.")

my_car = Car("Toyota", "Corolla", 2020)
my_car2 = Car("Hyundai", "Sonota", 2014)
my_car.display_info()  # Output: This car is a 2020 Toyota Corolla.
my_car.plate_number()
print( )
my_car2.display_info()  # Output: This car is a 2020 Toyota Corolla.
my_car2.plate_number()