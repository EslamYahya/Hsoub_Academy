from abc import ABC, abstractmethod
class OperatinSystem (ABC):
    def __init__(self):
        pass

    @abstractmethod
    def print_os(self):
        pass

class Windows(OperatinSystem):
    def __init__(self):
        pass

    def print_os(self):
        print("OS is windows")

class IOS(OperatinSystem):
    def __init__(self):
        pass

    def print_os(self):
        print("OS is IOS")

class Android(OperatinSystem):
    def __init__(self):
        pass

    def print_os(self):
        print("OS is Android")

x = Android()
x.print_os()