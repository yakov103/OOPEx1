from elevator import Elevator
from callForElevator import CallForElevator
from building import Building


class ElevatorController:

    def __init__(self,calls:[CallForElevator], build:Building):
        self._b = build
        self._elevators = self._b._elevators
        self._calls = calls

    def runAlgo (self):
         for c in self._calls:
            self.resetDoneElevators(c.time)
            ans = self.getCall(c)
            c.pushOrder(ans.getID())


    def resetDoneElevators (self, time):
        for elev in self._elevators:
            if elev._finishTime <= time :
                elev.resetElev()


    def getCall(self, c:CallForElevator) -> Elevator:
        bestElev = Elevator
        if c.elevator != -1:
            bestElev = self._elevators[c.elevator]
            return bestElev
        best = 100000
        cost = 0
        for elev in self._elevators:
            cost= 0
            if elev._b != None:
                cost += elev.calculateFloor(elev._b, c.src)
                cost += elev._leftTimer
            else :
                cost += elev.calculateFloor(c.src, c.dest)
                cost += elev.calculateFloor(elev.getPos(), c.dest)
            if (cost < best ):
                best = cost
                bestElev = elev
        bestElev.setOrder(c)
        bestElev._b = c.dest
        return bestElev




