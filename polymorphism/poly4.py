class Dog:
    def sound(self):
        print("Dog barks")

class cat:
    def sound(self):
        print("cat meows")

def make_sound(obj):
    obj.sound()

d = Dog()
c = cat()

make_sound(d)
make_sound(c)