
# OOP Assignment 1 at Ariel University. 
#### Offline Algorithem of Destination Dispatch Elevator
#### made by Yakov Khodorkovski and Nir Meir .

### Introduction :
Elevator with controling system are made for Optimization building with multiple floors that collect passengers to the Same destination.
Unike the regular Elevator , the smart Elevator with controling system can calculat the optimal Elevator for each people .


### Files : 
  * Ex1.py
  * building.py
  * callForElevator.py
  * elevator.py
  * elevatorController.py

  the main file is ```Ex1.py``` that load the ```building.json, class.csv ``` and return ``` output.csv ``` with results.

  the ```building.csv```, ```callForElevator.py ``` and ```elevator.py``` are collecting the data from the .json and .csv files to implement the Algorithem. 
  
  the core process of the algorithem is in the ```elevatorController.py``` , 
  the class elevatorController is implementing the building ( include the list of the elevators )  and the calls. 
  then , the ```runAlgo()``` functions is running the algorithm on all calls and selects the optimal elevator for each call by using a smart simulator that simulate the movement of the elevator by their characteristics and the calls from the user . 


  

  







## algorithm 
The algorithm gets a call, and need to choose the optimal elevator for the passenger.

```
   def getCall(self, c:CallForElevator) -> Elevator:
        bestElev = Elevator
        best = MAX.VALUE
        cost = 0
        for elev in self._elevators:
            cost= 0
            if elev._b != None:  # the elevator has calls except that one .
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
```
the calculateFloor function is a calculator that returns how much time will the call take , depending on how many floors and the elevator characteristics. 

The algorithm is greedy but it calculates very accurately the cost of travel, so it is an optimal solution for the assignment. 



## UML

![App Screenshot](https://i.ibb.co/M7LnR6N/UML.png)

 ## Bibliography

We used the links below to understand the problem in depth and formulate an algorithm that will lead to optimal performance.
 - [ETD Algorithm with Destination Dispatch and Booster Options](https://peters-research.com/index.php/papers/etd-algorithm-with-destination-dispatch-and -booster-options/)
 - [A Heuristic for the Situational Application of a Destination Dispatch Elevator System](https://github.com/do-ryan/destination-dispatch-elevator-simulation/blob/master/A%20Heu ristic%20for%20the%20Situational%20Application%20of%20a%20Destination%20Dispat ch%20Elevator%20System.pdf)
 - [Elevator selection with destination control system](https://global.ctbuh.org/resources/papers/download/1050-elevator-selection-with-d
estination-control-system.pdf)

