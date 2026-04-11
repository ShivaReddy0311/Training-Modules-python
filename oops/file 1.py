class student:
    def __init__(self,name="unknown", marks=0):
        self.name = name
        self.marks = marks
        
s1 = student()
s2 = student("shiva", 36)        

print(s1.name, s1.marks)
print(s2.name, s2.marks)