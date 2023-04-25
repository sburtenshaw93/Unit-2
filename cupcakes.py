from abc import ABC
from pprint import pprint
class Vehicle(ABC):
    pass

import csv

class Cupcake:
    size = "regular"
    def __init__(self, id, name, price, flavor, frosting, filling):
        self.id = id
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
    
    def __init__(self, id, name, price, flavor, frosting):
        self.id = id
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
    size = "Large"
    
    def calculate_price(self,quantity):
        return quantity * self.price
    
my_cupcake_mini = Mini("mini-chocolate-cupcake", "Chocolate", 1.99, "Chocolate", "Whip Cream")
print(my_cupcake_mini.name)    
print(my_cupcake_mini.price)  
print(my_cupcake_mini.size)  
    


def read_csv(file):
    with open("sample.csv") as csvfile:
        reader = csv.DictReader(csvfile)
    
        for row in reader:
            pprint(row)
read_csv("sample_csv")        

cupcake1 = Regular("vanilla-cupcake", "Vanilla", 3.99, "Vanilla", "Vanilla", "Whip Cream")
cupcake2 = Regular("chocolate-cupcake", "Chocolate Dream", 3.99, "Chocolate Dream", "Chocolate Fudge", "Chocolate Pudding")
cupcake3 = Large("cookies-and-cream-cupcake", "Oreo", 4.99, "Oreo", "Oreo Whip Cream", "Oreo Whip Cream")
cupcake3.add_sprinkles("Oreo Crumbles")
cupcake4 = Large("strawberry-cupcake", "Strawberry", 4.99, "Strawberry", "Strawberry Cream Cheese", "Fresh Strawberries")
cupcake5 = Mini("birthday-cupcake", "Red, White and Blue", 1.99, "Red White and Blue", "Blue Cream Cheese Frosting")
cupcake5.add_sprinkles("Red, White and Blue Sprinkles")
cupcake6 = Mini("red-velvet-cupcake", "Red Velvet", 1.99, "Red Velvet", "Cream Cheese")
cupcake7 = Mini("peanut-butter-cupcake", "Peanut Butter", 1.99, "Peanut Butter Cup", "Peanut Butter Whip")
cupcake7.add_sprinkles("Reeses Peanut Butter Cups")

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
        fieldnames = ["id", "size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"id": cupcake.id, "size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "filling": cupcake.filling, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"id": cupcake.id, "size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})
write_new_csv("sample.csv", cupcake_list)
                
def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if hasattr(cupcake, "filling"):
            writer.writerow({"id": cupcake.id, "size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles, "filling": cupcake.filling })
        else:
            writer.writerow({"id": cupcake.id, "size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})
            
def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
        return None
    
def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:   
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
         
print("CSV has created a new file")