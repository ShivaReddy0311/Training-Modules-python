class person:
    def details(self):
        print("person details")

class Employeee(person):
    def details(self):
        print("Employee details")

class Manager(Employee):
    def details(self):
        print("Manager details")

p = person()
e = Employee()
m = manager()

p.details()
e.details()
m.details()