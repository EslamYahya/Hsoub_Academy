from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any

class Builder(ABC):
    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass

class CarBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Car()

    @property
    def product(self) -> Car:
        car = self._product
        self.reset()
        return car

    def produce_part_a(self) -> None:
        self._product.add("PartACar")

    def produce_part_b(self) -> None:
        self._product.add("PartBCar")

    def produce_part_c(self) -> None:
        self._product.add("PartCCar")

class CarManualBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Manual()

    @property
    def product(self) -> Car:
        manual = self._product
        self.reset()
        return manual

    def produce_part_a(self) -> None:
        self._product.add("PartAManual")

    def produce_part_b(self) -> None:
        self._product.add("PartBManual")

    def produce_part_c(self) -> None:
        self._product.add("PartCManual")

class Car():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Car parts: {', '.join(self.parts)}", end="")

class Manual():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Manual parts: {', '.join(self.parts)}", end="")

class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder


    def build_basic_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

if __name__ == "__main__":
    CarDirector = Director()
    ManualDirector = Director()

    CarBuilder = CarBuilder()
    ManualBuilder = CarManualBuilder()

    CarDirector.builder = CarBuilder
    ManualDirector.builder = ManualBuilder

    print("Standard basic car: ")
    CarDirector.build_basic_product()
    CarBuilder.product.list_parts()
    print("\n")

    print("Standard basic carManual: ")
    ManualDirector.build_basic_product()
    ManualBuilder.product.list_parts()
    print("\n")

    print("Standard full featured Car: ")
    CarDirector.build_full_featured_product()
    CarBuilder.product.list_parts()
    print("\n")

    print("Standard full featured carManual: ")
    ManualDirector.build_full_featured_product()
    ManualBuilder.product.list_parts()
    print("\n")

    print("Custom car: ")
    CarBuilder.produce_part_a()
    CarBuilder.produce_part_b()
    CarBuilder.product.list_parts()
    print("\n")

    print("Custom carManual: ")
    ManualBuilder.produce_part_a()
    ManualBuilder.produce_part_b()
    ManualBuilder.product.list_parts()