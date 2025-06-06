from __future__ import annotations
from abc import ABC, abstractmethod

class AudioPlayer :
    def __init__(self) -> None:
        self.state: State = ReadyState(self)
      
    def changeState(self,state):
        self.state = state
    
    def clickLock(self) :
        self.state.clickLock()
    
    def clickPlay(self) :
        self.state.clickPlay()
    
    def clickNext(self) :
        self.state.clickNext()
    
    def clickPrevious(self) :
        self.state.clickPrevious()

    def nextSong(self):
        print("nextSong")

    def previousSong(self):
        print("previousSong")

    def fastForward(self,value):
        print("fastForward",value)

    def rewind(self,value):
        print("rewind",value)

class State(ABC):
    def __init__(self,player: AudioPlayer)  :
        self.player = player

    @abstractmethod
    def clickLock(self):
        pass

    @abstractmethod
    def clickPlay(self):
        pass

    @abstractmethod
    def clickNext(self):
        pass

    @abstractmethod
    def clickPrevious(self):
        pass

class LockedState (State):
    def __init__(self,player: AudioPlayer)  :
        super().__init__(player)

    def clickLock(self):
        print("Audio is already locked")

    def clickPlay(self):
        print("clickPlay from LockedState, Do nothing")

    def clickNext(self):
        print("clickNext from LockedState, Do nothing")

    def clickPrevious(self):
        print("clickPrevious from LockedState, Do nothing")

class ReadyState (State)  :
    def __init__(self,player: AudioPlayer)  :
        super().__init__(player)

    def clickLock(self):
        print("clickLock from ReadyState")
        self.player.changeState( LockedState(self.player))

    def clickPlay(self):
        print("clickPlay from ReadyState")
        self.player.changeState( PlayingState(self.player))

    def clickNext(self):
        print("clickNext from ReadyState")
        self.player.nextSong()

    def clickPrevious(self):
        print("clickPrevious from ReadyState")
        self.player.previousSong()

class PlayingState (State)  :
    def __init__(self,player: AudioPlayer)  :
        super().__init__(player)

    def clickLock(self):
        print("clickLock from PlayingState")
        self.player.changeState( LockedState(self.player))

    def clickPlay(self):
        print("clickPlay from PlayingState")
        self.player.changeState( ReadyState(self.player))

    def clickNext(self):
        print("clickNext from PlayingState")
        if (True): 
            self.player.nextSong()
        else:
            self.player.fastForward(5)

    def clickPrevious(self):
        print("clickPrevious from PlayingState")
        if (True): 
            self.player.previousSong()
        else:
            self.player.rewind(5)

if __name__ == "__main__":
    audioPlayer = AudioPlayer()

    audioPlayer.clickPlay()
    audioPlayer.clickNext()
    audioPlayer.clickPrevious()
    audioPlayer.clickLock()

    playingState= PlayingState(audioPlayer)
    audioPlayer.changeState(playingState)
    audioPlayer.clickPlay()
    audioPlayer.clickNext()
    audioPlayer.clickPrevious()
    audioPlayer.clickLock()

    lockedState= LockedState(audioPlayer)
    audioPlayer.changeState(lockedState)
    audioPlayer.clickPlay()
    audioPlayer.clickNext()
    audioPlayer.clickPrevious()
    audioPlayer.clickLock()
