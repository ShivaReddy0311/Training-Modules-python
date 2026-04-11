class grandparent():
    def vehicle_name(self):
        print("koenigsegg")
class parent(grandparent):
    def car_model(self):
        print("JESKO")
class child(parent):
    def car_speed(self):
        print("531KMPH")
c=child()

c.vehicle_name()
c.car_model()
c.car_speed()