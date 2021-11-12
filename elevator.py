

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


    def getState(self) -> int:
        return self._direction

    def getSpeed(self) -> float:
        return self._speed

    def getPos(self)-> int:
        return self._position