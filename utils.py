import math
from elevator import Elevator
from callForElevator import CallForElevator


@staticmethod
def calculateTravel(elev:Elevator, startFloor:int, finishFloor:int )-> int:
    x = abs(finishFloor - startFloor)
    y =  abs(finishFloor-startFloor)/elev.getSpeed()
    return x+y


#func can be much better, need improvement
def calculatePostionsTime (elev:Elevator, calls:[CallForElevator], c:CallForElevator):  #c is num of call
    pos = elev.getPos()
    idOfCall = c.id
    if idOfCall != 0 :
        timePassed = abs(c.time - elev._timePostion)
        pos = timePassed *elev.getSpeed()
    return pos

def countStops (elev:Elevator, calls:[CallForElevator], c:CallForElevator):
    counter = 0
    if (len(calls) > 0 and c.src < c.dest):
        numOfCall = c.id
        for i in range(0, numOfCall):
            if (calls[i].elevator == elev._id):
                if (calls[i].src <= c.src <= calls[i].dest):
                        counter = counter + 1
                if (calls[i].src <= c.dest <= calls[i].dest):
                        counter = counter + 1
    if (len(calls) > 0 and c.src >= c.dest):
        numOfCall = c.id
        for i in range(0, numOfCall):
            if (calls[i].elevator == elev._id):
                if (calls[i].src >= c.src >= calls[i].dest):
                    counter = counter + 1
                if (calls[i].src >= c.dest >= calls[i].dest):
                    counter = counter + 1
    return counter





