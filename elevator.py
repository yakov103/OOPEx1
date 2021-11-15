from callForElevator import CallForElevator

class Elevator:
    def __init__(self, id):
        self._id = int(id["_id"])
        self._speed = float(id["_speed"])
        self._minFloor = int(id["_minFloor"])
        self._maxFloor = int(id["_maxFloor"])
        self._closeTime = float(id["_closeTime"])
        self._openTime = float(id["_openTime"])
        self._startTime = float(id["_startTime"])
        self._stopTime = float(id["_stopTime"])
        self._direction = 0
        self._position  = 0.0
        self._timePostion = 0.0
        self._callsUp = []
        self._callsDown = []

    def costStop(self):
        return self._openTime + self._stopTime + self._startTime +self._closeTime

    def getState(self) -> int:
        return self._direction

    def getSpeed(self) -> float:
        return self._speed

    def getPos(self)-> int:
        return self._position

    def __eq__(self, other):
        if isinstance(other, Elevator):
            return self._id == other._id


    def __lt__(self, other)-> bool:
        return self._id < other._id

    def updatePos (self, posElev:float , posTime :float):
        self._position=posTime
        self._timePostion = posTime


