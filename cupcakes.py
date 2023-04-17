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
my_cupcake = Cupcake("Cookies and Cream", 2.99, "Chocolate", "Oreo", "Vanilla")

my_cupcake.add_sprinkles("Oreo crumbs", "Chocolate", "Vanilla")

print(my_cupcake.sprinkles)

print("------------------Changing Cupcake---------------------")
my_cupcake.frosting = "Chocolate"
my_cupcake.filling = "Chocolate"
my_cupcake.name = "Triple Choclate"

my_cupcake.is_miniature = False
print(my_cupcake.is_miniature)

print(my_cupcake)
        