class Book:
    def __init__(self, price):
        self.price = price

    def __add__(self, other):
        return self.price + other.price
b1 = Book(200)
b2 = Book(150)
print("total price", b1 + b2)