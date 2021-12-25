from unittest import TestCase

from Ex1 import readCalls
from building import Building
from elevatorController import ElevatorController


class tests(TestCase):

    def test_1(self):
        '''
        test 1 is for checking which is best .
        there are 2 calls, bringing up the both elevators , and than adding 2 calls down ,
        that need to be alocated to 1 the faster elevator .
        :return:
        '''
        b = Building("B2.json")
        calls = readCalls("test_calls.csv", b)
        controller = ElevatorController(calls, b)
        controller.runAlgo()
        self.assertEqual(controller._calls[0].elevator, 1)
        self.assertEqual(controller._calls[1].elevator, 0)
        self.assertEqual(controller._calls[2].elevator, 1)
        self.assertEqual(controller._calls[3].elevator, 1)

    def test_2(self):
        '''
        test 2 is a big building (-10,100)
        elevator 1 is much faster , we let him go up , than check if the slowest(0) take a very close call  .
        :return:
        '''
        b = Building("B3.json")
        calls = readCalls("test_calls_1.csv", b)
        controller = ElevatorController(calls, b)
        controller.runAlgo()
        self.assertEqual(controller._calls[0].elevator, 1)
        self.assertEqual(controller._calls[1].elevator, 1)
        self.assertEqual(controller._calls[2].elevator, 1)
        self.assertEqual(controller._calls[3].elevator, 0)
