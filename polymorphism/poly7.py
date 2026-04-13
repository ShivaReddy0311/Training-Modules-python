class person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __add__(self, other):
        return self.first +""+other.last

p1 = person("Akash","A")
p2 = person("king","akash")
print("Full Name",p1 + p2)