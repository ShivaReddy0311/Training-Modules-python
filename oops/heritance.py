class person():
    def greet(self):
        print("hello from person")
class student(person):
    def student(self):
        print("student is studiying")
class employee(person):
    def work(self):
        print("employee is working")
s = student()
e = employee()
s.greet()
s.student()
e.work()
