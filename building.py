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

    # def getCall(self, calls:[CallForElevator], c:CallForElevator) -> int:
    #     best = 10000000.0
    #     ans = 0
    #     savePos = float
    #     for i in self._elevators:
    #         i.updatePos(i.getPos(), calls[c.id].time)
    #         UpdatePostion(i,calls,c)
    #
    #     if (len(self._elevators) > 1 ):
    #         for i in range(len(self._elevators)):
    #             cost =0
    #            # pos = calculatePostionsTime (self._elevators[i],calls ,c )
    #             cost = calculateTravel (self._elevators[i], self._elevators[i].getPos(), c.src)
    #             cost = cost + countStops(self._elevators[i],calls, c)
    #             if (cost <= best):
    #                 ans = i
    #                 best = cost
    #              #   savePos = pos
    #
    #     if (c.src <= c.dest):
    #         self._elevators[ans]._direction = 1
    #
    #     if (c.src >= c.dest):
    #         self._elevators[ans]._direction = -1
    #
    #     #self._elevators[ans].updatePos(savePos,c.time)
    #
    #     return ans
    #
    # def runAlgo (self, calls:[CallForElevator]):
    #      for i in range(0,len(calls)):
    #          calls[i].elevator = self.getCall(calls,calls[i])
    #      return calls


