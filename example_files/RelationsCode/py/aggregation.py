class Manager:
    def __init__(self, name):
        self.name = name
        print(name + " manages the collage")

class Collage:
    def __init__(self, manager):
        self.manager = manager

manager = Manager("Dr. Ahmad")
collage = Collage(manager)
