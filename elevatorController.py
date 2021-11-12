from elevator import Elevator
from callForElevator import CallForElevator
from utils import calculateFloorPassCost

import heapq


class ElevatorController:

    def __init__(self):
        self.callsUp =[]
        heapq.heapify(self.callsUp)           # for a min heap
        self.callsDown = []
        heapq._heapify_max(self.callsDown)    #for a maxheap
        self.stopsForEachFloor=[int]
        self._direction = 0


    def calculateTravel(self, elev:Elevator,c:CallForElevator ):
        cost = 0.0;
        cost = cost + calculateFloorPassCost(elev, elev.getPos(), c.src)
        #need to add calcuate stops
        return cost


    def pushanOrder (self,c : CallForElevator ):
        if (c.dest >= c.src):
            heapq.heappush(self.callsUp,c.src)
            heapq.heappush(self.callsUp,c.dest)
        else:
            heapq._heappush_max(self.callsUp,c.src)
            heapq._heappush_max(self.callsUp, c.dest)




