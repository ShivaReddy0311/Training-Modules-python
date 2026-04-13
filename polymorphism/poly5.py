class caluculator:
    def add(self,a,b,c=0):
        return a + b + c
calc = caluculator()
print(calc.add(10,20))
print(calc.add(10, 20, 30))