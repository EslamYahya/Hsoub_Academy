from abc import ABC, abstractmethod

class Strategy (ABC):
    @abstractmethod
    def execute(self,a,b):
        pass

class ConcreteSTAdd(Strategy):
    def execute(self, a,b):
        return a+b

class ConcreteSTSubtract(Strategy):
    def execute(self, a,b):
        return a-b

class ConcreteSTMultiple(Strategy):
    def execute(self, a,b):
        return a*b


class Context:
    def __init__(self, strategy: Strategy)  :
        self._strategy = strategy

    def setStrategy(self,s:Strategy)  :
        self._strategy = strategy

    def executeStrategy(self,a,b)  :
        print(self._strategy.execute(a,b))


if __name__ == "__main__":

    context = Context(ConcreteSTAdd())
    print ("Strategy Add:",2,"and", 5)
    context.executeStrategy(2,5)

    context = Context(ConcreteSTMultiple())
    print ("Strategy Multiple:",2,"and", 5)
    context.executeStrategy(2,5)

    context = Context(ConcreteSTSubtract())
    print ("Strategy Subtract:",2,"and", 5)
    context.executeStrategy(2,5)
