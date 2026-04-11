class person():
    def animal(self):
        print("method of sound")
class Dog(person):
    def dog(self):
        print("bark")
class cat(person):
    def cat(self):
        print("meow")


e =Dog()
s =cat()
s.animal()
e.dog()
s.cat()
