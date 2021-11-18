import math
from callForElevator import CallForElevator

class Elevator:

    UP = 1
    LEVEL = 0
    DOWN = 0

    def __init__(self, id):
        self._id = int(id["_id"])
        self._speed = float(id["_speed"])
        self._minFloor = int(id["_minFloor"])
        self._maxFloor = int(id["_maxFloor"])
        self._closeTime = float(id["_closeTime"])
        self._openTime = float(id["_openTime"])
        self._startTime = float(id["_startTime"])
        self._stopTime = float(id["_stopTime"])
        self._direction = Elevator.LEVEL
        self._position = 0
        self._leftTimer = 0.0
        self._finishTime = 0.0
        self._a= None
        self._b= None

    def costStop(self):
        return self._openTime + self._stopTime + self._startTime +self._closeTime

    def getID(self):
        return self._id

    def addStop(self):
        self._leftTimer += self.costStop()
        self._finishTime += self.costStop()

    def getState(self) -> int:
        return self._direction

    def getSpeed(self) -> float:
        return self._speed

    def getPos(self)-> int:
        return self._position

    def setOrder (self, c:CallForElevator):
        self._a = c.src
        self._b = c.dest
        self._leftTimer += self.calculateFloor(self.getPos(), c.src) + self.calculateFloor(c.src, c.dest)
        self._finishTime = self._leftTimer + c.time
        if c._direction == Elevator.UP:
            self._direction = Elevator.UP
        else:
            self._direction = Elevator.DOWN



    def calculateFloor (self, startPoint:int , finishPoint:int):
        timeToMove = self._openTime + self._closeTime+ self._startTime + self._stopTime
        floorPassed = abs (startPoint - finishPoint)
        return timeToMove + floorPassed/self.getSpeed()

    def resetElev (self):
        self._a = None
        self._b = None
        self._position = 0
        self._leftTimer = 0.0
        self._direction = Elevator.LEVEL


    def __eq__(self, other):
        if isinstance(other, Elevator):
            return self._id == other._id


    def __lt__(self, other)-> bool:
        return self._id < other._id

    def updatePos (self, posElev:float , posTime :float):
        self._position=posElev
        self._timePostion = posTime


