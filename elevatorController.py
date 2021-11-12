from elevator import Elevator
from callForElevator import CallForElevator
from utils import calculateFloorPassCost

import heapq
import queue

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
            heapq.heappush(self.callsDown,c.src)
            heapq.heappush(self.callsDown,c.dest)
            heapq._heapify_max(self.callsDown)


    def navigateElevator(self,curr:Elevator):
        if (curr.getState() == 0 ):
            if (self._direction == 1):
                if(len(self.callsUp) != 0 ):
                pass

            if (self._direction == -1):
            pass

        pass
