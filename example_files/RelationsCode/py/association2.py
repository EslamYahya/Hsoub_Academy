class Driver:
    def __init__(self):
        pass
    print("driver is ready")

class Car:
    def __init__(self, driven_by):
        self.driven_by = driven_by
    print("car is driven by the driver")
    
driver = Driver()
car = Car(driver)
