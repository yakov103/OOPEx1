import random

from elevator import Elevator
from callForElevator import CallForElevator
import json



class Building:
    def __init__(self, file_name):
        with open (file_name, 'r') as f:
            details = json.load(f)
            self._minFloor = int(details["_minFloor"])
            self._maxFloor = int(details["_maxFloor"])
            self._elevators = []
            for i in details["_elevators"]:
                self._elevators.append(Elevator(i))


    def __str__(self):
        return f"just for test : min floor is {self._minFloor} and num of lifts is {len(self._elevators)}"

    def getElevators (self) -> [Elevator]:
        return self._elevators
