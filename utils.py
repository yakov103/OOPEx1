import math
from elevator import Elevator

@staticmethod
def calculateFloorPassCost(elev:Elevator, startFloor:int, finishFloor:int )-> int:
    return abs(finishFloor - startFloor)+ abs(finishFloor-startFloor)/elev.getSpeed()

