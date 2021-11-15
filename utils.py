import math
from elevator import Elevator
from callForElevator import CallForElevator


@staticmethod
def calculateTravel(elev:Elevator, startFloor:int, finishFloor:int )-> int:
    return abs(finishFloor - startFloor)+ abs(finishFloor-startFloor)/elev.getSpeed()


#func can be much better, need improvement
def calculatePostionsTime (elev:Elevator, calls:[CallForElevator], c:CallForElevator):  #c is num of call
    timePassed = c.time - elev._timePostion
    counter =0.0
    stops =float
    pos = elev.getPos()
    if (elev.getState() != 0 ):
        pos = pos + timePassed*(elev.getSpeed())
        for i in range(0,c.id):
            if (calls[i].elevator == elev._id and elev.getState() == 1 and calls[i].dest < c.dest and calls[i].dest >= elev.getPos() ):
                coutner = counter + 1
            if (calls[i].elevator == elev._id and elev.getState() == -1 and calls[i].dest > c.dest and calls[i].dest <= elev.getPos() ):
                coutner = counter + 1

        pos = pos + counter*(elev.costStop())

    return pos





