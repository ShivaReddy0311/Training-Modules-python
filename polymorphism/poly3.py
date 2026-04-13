class vehicle:
    def start(self):
        print("vehicle starting")

class car(vehicle):
    def start(self):
        print("car enginr starting")

v = vehicle()
c = car()

v.start()
c.start()