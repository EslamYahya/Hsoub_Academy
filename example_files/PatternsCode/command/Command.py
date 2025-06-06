from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self, app: Application, editor: Editor):
        self._app = app
        self._editor = editor
        self._backup = None

    # Make a backup of the editor's state.
    def saveBackup(self) :
        print("SaveBuckup")
        self._backup = self._editor.text

    # Restore the editor's state.
    def undo(self) :
        print("undo")
        self._editor.text = self._backup

    @abstractmethod
    def execute(self)  :
        pass

    def __str__(self):
        return str(self.__class__)

class CopyCommand (Command)  :
    def __init__(self, app: Application, editor: Editor):
        super().__init__( app, editor)

    def execute(self) :
        print("CopyCommand executed")
        self._app.clipboard = self._editor.getSelection()
        return False

class CutCommand  (Command)  :
    def __init__(self, app: Application, editor: Editor):
        super().__init__( app, editor)

    def execute(self) :
        print("CutCommand executed")
        self.saveBackup()
        self._app.clipboard = self._editor.getSelection()
        self._editor.deleteSelection()
        return True

class PasteCommand  (Command)  :
    def __init__(self, app: Application, editor: Editor):
        super().__init__( app, editor)

    def execute(self) :
        print("PasteCommand executed")
        self.saveBackup()
        self._editor.replaceSelection(self._app.clipboard)
        return True

class UndoCommand  (Command)  :
    def __init__(self, app: Application, editor: Editor):
        super().__init__( app, editor)

    def execute(self) :
        print("UndoCommand executed")
        self._app.executeUndo()
        return False

class CommandHistory :
    def __init__(self ):
        self.__history:List[Command] = []

    def push(self,c: Command) :
        print("push CommandHistory")
        self.__history.append(c)

    def pop(self) -> Command :
        print("pop CommandHistory")
        return self.__history.pop()