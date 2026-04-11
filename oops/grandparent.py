class grandparent:
    def greet_grandparent(self):
        print("helooo from grandparent")
class parent(grandparent):
    def greet_parent(self):
        print("hello from parent")
class child(parent):
    def greet_child(self):
        print("hello from child")
c=child()
c.greet_grandparent()
c.greet_parent()
c.greet_child()