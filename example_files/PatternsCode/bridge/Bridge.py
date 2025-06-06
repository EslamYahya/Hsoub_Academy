from __future__ import annotations
from abc import ABC, abstractmethod

class RemoteControl:
    def __init__(self, device : Device):
        self._device = device

    def togglePower(self):
        if self._device.isEnabled():
            self._device.disable()
        else:
            self._device.enable()

    def volumeDown(self):
        self._device.setVolume(self._device.getVolume() - 10)

    def volumeUp(self):
        self._device.setVolume(self._device.getVolume() + 10)

    def channelDown(self):
        self._device.setChannel(self._device.getChannel() - 1)

    def channelUp(self):
        self._device.setChannel(self._device.getChannel() + 1)

class AdvancedRemoteControl (RemoteControl):
    def mute(self):
        self._device.setVolume(0)
        print("device muted")

class Device (ABC):
    @abstractmethod
    def isEnabled(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def getVolume(self):
        pass

    @abstractmethod
    def setVolume(self,percent):
        pass

    @abstractmethod
    def getChannel(self):
        pass

    @abstractmethod
    def setChannel(self,channel):
        pass

class TV(Device):
    def isEnabled(self):
        print("From Tv, isEnabled")
        return True

    def enable(self):
        print("From Tv, enable")

    def disable(self):
        print("From Tv, disable")

    def getVolume(self):
        return "From Tv, volume"

    def setVolume(self,percent):
        print("From Tv, setVolume")

    def getChannel(self):
        return "From Tv, Channel"

    def setChannel(self,channel):
        print("From Tv, setChannel")


class Radio(Device):
    def isEnabled(self):
        print("From Radio, isEnabled")
        return True

    def enable(self):
        print("From Radio, enable")

    def disable(self):
        print("From Radio, disable")

    def getVolume(self):
        return "From Radio, volume"

    def setVolume(self, percent):
        print("From Radio, setVolume")

    def getChannel(self):
        return "From Radio, Channel"

    def setChannel(self, channel):
        print("From Radio, setChannel")


if __name__ == "__main__":
    tv = TV()
    remote = RemoteControl(tv)
    remote.togglePower()

    radio = Radio()
    remote = AdvancedRemoteControl(radio)
    remote.togglePower()