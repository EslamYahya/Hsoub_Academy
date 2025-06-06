class Car:
    def __init__(self):
        pass
    print("car is ready")

class Driver:
    def __init__(self, has_drive):
        self.has_drive = has_drive  
    print("driver drives the car")

car = Car()
driver = Driver(car)
