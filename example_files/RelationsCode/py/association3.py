class Car:
    def __init__(self):
        self.driven_by = None 
    print("car is driven by driver")
    
class Driver:
    def __init__(self, has_drive):
        self.has_drive = has_drive
        self.has_drive.driven_by = self
    print("driver drives a car")


car = Car()
driver = Driver(car)
