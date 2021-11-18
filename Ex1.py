import csv
import csvwriter as csvwriter
from building import Building
from callForElevator import CallForElevator
from elevatorController import  ElevatorController
import sys


def readCalls(file_name:str,b:Building):
    callsList = []
    with open(file_name) as f:
        data = csv.reader(f)
        j =0
        for i in data:
            callsList.append(CallForElevator(i,j))
            j = j + 1

    return callsList


def writeAns(ansCalls:dict, file_name:str):
    anslist =[]
    for i in ansCalls:
        anslist.append(i.__dict__.values())
    with open(file_name, 'w', newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(anslist)


if __name__ == '__main__':

    b = Building(sys.argv[1])
    calls = readCalls(sys.argv[2],b)
    controller = ElevatorController(calls,b)
    controller.runAlgo()
    writeAns(controller._calls,sys.argv[3])
