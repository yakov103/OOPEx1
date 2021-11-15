from elevator import Elevator
from callForElevator import CallForElevator

from building import Building
import heapq
import queue

class ElevatorController:

    def __init__(self):
       self._UpCalls = []
       self._DownCalls = []


