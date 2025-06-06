from __future__ import annotations
from abc import ABC, abstractmethod
 
class Dialog(ABC):
    @abstractmethod
    def create_button(self):
        # شيفرة افتراضية
        pass

    def dialogRender(self) -> str:
        OkButton = self.create_button()
        result = f"Dialog: {OkButton.render()}"
        return result
 
class WindowsDialog(Dialog):
    def create_button(self) -> WindowsButton:
        return WindowsButton()
 
class MacDialog(Dialog):
    def create_button(self) -> MacButton:
        return MacButton()
 
class LinuxDialog(Dialog):
    def create_button(self) -> LinuxButton:
        return LinuxButton()
 

class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass
 
class WindowsButton(Button):
    def render(self) -> str:
        return "{Result of the Windowsbutton}"
 
class MacButton(Button):
    def render(self) -> str:
        return "{Result of the Macbutton}"
 
class LinuxButton(Button):
    def render(self) -> str:
        return "{Result of the Linuxbutton}"
 
 
def client_code(dialog: Dialog) -> None:
    print(f"Client: I'm not aware of the Dialog's class.\n"
          f"{dialog.dialogRender()}", end="")

if __name__ == "__main__":
    print("App: Launched with the WindowsDialog.")
    client_code(WindowsDialog())
    print("\n")
    print("App: Launched with the MacDialog.")
    client_code(MacDialog())
    print("\n")
    print("App: Launched with the LinuxDialog.")
    client_code(LinuxDialog())
 
