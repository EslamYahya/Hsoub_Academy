class Animal:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description

    def eating(self):
        print(self.__name, "is eating")

class Duck(Animal):
    def __init__(self, name, description):
        super().__init__(name, description)

    def float(self):
        print("The Duck is floating")

class Crocodile(Animal):
    def __init__(self, name, description):
        super().__init__(name, description)

    def go_out_water(self):
        print("The Crocodile is go out water")

class Ostrich(Animal):
    def __init__(self, name, description):
        super().__init__(name, description)

    def head_bury(self):
        print("The Ostrich bury its head in sand")

crocodile = Crocodile("CoCo", "green color animal")
crocodile.go_out_water()
crocodile.eating()
print("==============")
Duck = Duck("food", "white")
Duck.float()
Duck.eating()
