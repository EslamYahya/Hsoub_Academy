from __future__ import annotations
import math

class RoundHole:
    def __init__(self, radius: int):
        self.__radius = radius

    def getRadius(self) -> int :
        return self.__radius

    def fits(self, peg:RoundPeg) -> bool:
        return self.getRadius() >= peg.getRadius()

class RoundPeg:
    def __init__(self, radius: int):
        self.__radius = radius

    def getRadius(self)-> int:
        return self.__radius

class SquarePeg:
    def __init__(self, width: int):
        self.__width = width

    def getWidth(self)-> int:
        return self.__width

class SquarePegAdapter (RoundPeg):
    def __init__(self, peg: SquarePeg):
        self.__peg = peg

    def getRadius(self):
        return self.__peg.getWidth() * math.sqrt(2)/2

if __name__ == "__main__":
    hole =   RoundHole(5)
    rpeg =   RoundPeg(5)
    print (hole.fits(rpeg))

    small_sqpeg = SquarePeg(5)
    large_sqpeg = SquarePeg(10)
    #print (hole.fits(small_sqpeg))  # this won't compile (incompatible types)

    small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
    large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)
    print (hole.fits(small_sqpeg_adapter))
    print (hole.fits(large_sqpeg_adapter))
