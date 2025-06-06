from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List
 
class Publisher:

    _state: int = None

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("publisher: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)


    def notify(self) -> None:

        print("publisher: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:

        print("\nPublisher: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Publisher: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):

    @abstractmethod
    def update(self, publisher: Publisher) -> None:
        pass


class ConcreteObserverA(Observer):
    def update(self, publisher: Publisher) -> None:
        if publisher._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, publisher: Publisher) -> None:
        if publisher._state == 0 or publisher._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    # The client code.

    publisher = Publisher()

    observer_a = ConcreteObserverA()
    publisher.attach(observer_a)

    observer_b = ConcreteObserverB()
    publisher.attach(observer_b)

    publisher.some_business_logic()
    publisher.some_business_logic()

    publisher.detach(observer_a)

    publisher.some_business_logic()
 