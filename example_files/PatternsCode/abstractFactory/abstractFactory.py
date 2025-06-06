from __future__ import annotations
from abc import ABC, abstractmethod

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

class Button(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass

class WinButton(Button):
    def useful_function_a(self) -> str:
        return "The result of the windows button."

class MacButton(Button):
    def useful_function_a(self) -> str:
        return "The result of the macOS button."

class Checkbox(ABC):
    @abstractmethod
    def useful_function_b(self) -> None:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: Button) -> None:
        pass

class WinCheckbox(Checkbox):
    def useful_function_b(self) -> str:
        return "The result of the windows Checkbox."

    def another_useful_function_b(self, collaborator: Button) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the windows Checkbox collaborating with the ({result})"

class MacCheckbox(Checkbox):
    def useful_function_b(self) -> str:
        return "The result of the product macOS Checkbox."

    def another_useful_function_b(self, collaborator: Button):
        result = collaborator.useful_function_a()
        return f"The result of the macOS Checkbox collaborating with the ({result})"

def client_code(factory: GUIFactory) -> None:
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(f"{checkbox.useful_function_b()}")
    print(f"{checkbox.another_useful_function_b(button)}", end="")


if __name__ == "__main__":
    print("Client: Testing client code with the Windows Factory:")
    client_code(WinFactory())
    print("\n")
    print("Client: Testing the same client code with the MacOS Factory:")
    client_code(MacFactory())