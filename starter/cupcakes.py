from abc import ABC
from pprint import pprint
class Vehicle(ABC):
    pass

import csv

class Cupcake:
    size = "regular"
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)   
            
    def calculate_price(self,quantity):
        return quantity * self.price
    
class Mini(Cupcake):
    size = "Mini"  
    
    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []
        
    def calculate_price(self,quantity):
        return quantity * self.price

class Regular(Cupcake):
    size = "Regular"
    
    def calculate_price(self,quantity):
        return quantity * self.price        

class Large(Cupcake):
    size = "Large "
    
    def calculate_price(self,quantity):
        return quantity * self.price
    
my_cupcake_mini = Mini("Chocolate", 1.99, "Chocolate", "White", "Whip Cream")
print(my_cupcake_mini.name)    
print(my_cupcake_mini.price)  
print(my_cupcake_mini.size)  
    


def read_csv(file):
    with open("sample.csv") as csvfile:
        reader = csv.DictReader(csvfile)
    
        for row in reader:
            pprint(row)
read_csv("sample_csv")        

cupcake1 = Regular("Vanilla", 3.99, "Vanilla", "Vanilla", "Whip Cream")
cupcake2 = Regular("Chocolate Dream", 2.75, "Chocolate", "Chocolate Fudge", "none", "Chocolate Pudding")
cupcake3 = Large("Oreo", 4.00, "Chocolate", "Oreo Whip Cream", "Oreo Crumbles", "Oreo Whip Cream")
cupcake4 = Mini("Red, White and Blue", 1.99, "Red Velvet", "Blue Cream Cheese Frosting", "Whip Cream")
cupcake4.add_sprinkles("Red, White and Blue Sprinkles")
cupcake5 = Large("Strawberry", 4.00, "Strawberry", "Strawberry Cream Cheese", "Fresh Strawberries", "Fresh Strawberries")
cupcake6 = Mini("Red Velvet", 1.99, "")
cupcake7 = 

cupcake_list = [
    cupcake1,
    cupcake2,
    cupcake3,
    cupcake4,
    cupcake5,
    cupcake6,
    cupcake7,
]
        
def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writerheader()
        
        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "sprinkles": cupcake.sprinkles})
write_new_csv("sample.csv", cupcake_list)
                
def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "sprinkles": cupcake.sprinkles})
            

        