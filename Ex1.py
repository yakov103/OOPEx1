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

    # for i in range(5):
    #     i += 1
    #     bString = f"B{i}.json"
    #     b = Building(bString)
    #     if i == 1 or i == 2 :
    #         callString = "Calls_a.csv"
    #         calls = readCalls(callString,b)
    #         controller = ElevatorController(calls, b)
    #         controller.runAlgo()
    #         writeAns(controller._calls,f"output_B{i}_a.csv")
    #     elif i > 2 :
    #         callString1 = "Calls_a.csv"
    #         callString2 = "Calls_b.csv"
    #         callString3 = "Calls_c.csv"
    #         callString4 = "Calls_d.csv"
    #         calls1 = readCalls(callString1, b)
    #         calls2 = readCalls(callString2, b)
    #         calls3 = readCalls(callString3, b)
    #         calls4 = readCalls(callString4, b)
    #         controller1 = ElevatorController(calls1, b)
    #         controller2 = ElevatorController(calls2, b)
    #         controller3 = ElevatorController(calls3, b)
    #         controller4 = ElevatorController(calls4, b)
    #         controller1.runAlgo()
    #         controller2.runAlgo()
    #         controller3.runAlgo()
    #         controller4.runAlgo()
    #         writeAns(controller1._calls, f"output_B{i}_a.csv")
    #         writeAns(controller2._calls, f"output_B{i}_b.csv")
    #         writeAns(controller3._calls, f"output_B{i}_c.csv")
    #         writeAns(controller4._calls, f"output_B{i}_d.csv")


    # b = Building(sys.argv[1])
    # calls = readCalls(sys.argv[2],b)
    # controller = ElevatorController(calls,b)
    # controller.runAlgo()
    # writeAns(controller._calls,sys.argv[3])

    b = Building("B2.json")
    calls = readCalls("test_calls.csv", b)
    controller = ElevatorController(calls, b)
    controller.runAlgo()
    writeAns(controller._calls, "test_output.csv")



