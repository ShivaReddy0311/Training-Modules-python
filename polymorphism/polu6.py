class Item:
    def __init__(self,price):
        self.price = price

    def __mu1__(self, other):
        return self.price * other.price

s1 = Item(55)
s2 = Item(100)
print("Total cost",)