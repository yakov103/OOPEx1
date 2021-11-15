
class CallForElevator:
    def __init__(self, call, id):
        self.name = call[0]
        self.time = float(call[1])
        self.src = int(call[2])
        self.dest = int(call[3])
        self.state =int(call[4])
        self.elevator = int(call[5])
        self._isDone = False;
        self.id = id


    def pushOrder (self, elev:int ):
        self.elevator = elev
