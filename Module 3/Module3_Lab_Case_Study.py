"""
Program name: Module 3 Lab Case Study
Author: Sameena Ghaswala
Purpose: To understand the concept of inheritance.
"""

class Vehicle:
    def __init__(self):
        self.type = "car"

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__()
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def vehicle_description(self):
        print(f"Vehicle Type: {self.type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")


in_year = int(input("Enter the year: "))
in_make = input("Enter the make: ")
in_model = input("Enter the model: ")
in_doors = int(input("Enter the doors (2 or 4): "))
in_roof = input("Enter the roof (solid or sun roof): ")
car = Automobile(in_year, in_make, in_model, in_doors, in_roof)
car.vehicle_description()