from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.required_operations2()
        self.base_operation3()

    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the most of the work")

    def base_operation2(self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")

    def base_operation3(self) -> None:
        print("AbstractClass says: But I am doing the most of the work anyway")

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

class ConcreteClass1(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")

    # optional overriding
    def base_operation1(self) -> None:
        print("ConcreteClass1 says: I am overriding base_operation1 in the interface for doing the most of the work")

    def base_operation2(self) -> None:
        print("ConcreteClass1 says: I am overriding base_operation2 in the interface")

    def base_operation3(self) -> None:
        print("ConcreteClass1 says: I am overriding base_operation3 in the interface for doing the most of the work anyway")

class ConcreteClass2(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    # optional overriding
    def base_operation1(self) -> None:
        print("ConcreteClass2 says: I am overriding base_operation1 in the interface for doing the most of the work")
        
def client_code(abstract_class: AbstractClass) -> None:
    # ...
    abstract_class.template_method()
    # ...

if __name__ == "__main__":
    print("Same client code can work with different subclasses, subclass1:")
    client_code(ConcreteClass1())
    print("")
    print("Same client code can work with different subclasses, subclass2:")
    client_code(ConcreteClass2())