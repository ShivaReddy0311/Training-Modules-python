class grandparent():
    def grandparent_name(self):
        print("shiva")
class parent(grandparent):
    def parent_salary(self):
        print("400000000")
class child(parent):
    def child_department(self):
        print("R&D")
c=child()

c.grandparent_name()
c.parent_salary()
c.child_department()