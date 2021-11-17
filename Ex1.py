import csv
import csvwriter as csvwriter
from building import Building
from callForElevator import CallForElevator
from elevatorController import  ElevatorController


def readCalls(file_name:str,b:Building):
    callsList = []
    with open(file_name) as f:
        data = csv.reader(f)
        j =0
        for i in data:
           # if(buildingSuitableCalls(b,i[2],i[3])):
            callsList.append(CallForElevator(i,j))
            j = j + 1

    return callsList


def writeAns(ansCalls:dict):
    anslist =[]
    for i in ansCalls:
        anslist.append(i.__dict__.values())
    with open("output.csv", 'w', newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(anslist)



def  buildingSuitableCalls (b : Building,src:int,dest:int )->bool:
    flag1 = src >= b._minFloor and src <= b._maxFloor
    flag2 = dest >= b._minFloor and dest <= b._maxFloor
    return flag1 and flag2


if __name__ == '__main__':

    b = Building("B5.json")
    calls = readCalls("Calls_d.csv",b)
    controller = ElevatorController(calls,b)
    controller.runAlgo()
    writeAns(controller._calls)
