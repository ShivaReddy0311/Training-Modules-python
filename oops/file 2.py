class fan:
    def __init__(self,name,brand,price):
       self.name = name
       self.brand = brand
       self.price = price

# creating object
s1 = fan ("fan","usha", 3000)
s2 = fan ("fan","akash", 90000)     

print(s1.name)
print(s1.brand)
print(s1.price)
print(s2.name)
print(s2.brand)
print(s2.price)