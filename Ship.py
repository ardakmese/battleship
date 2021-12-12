from enum import Enum
import random

class AllShips(Enum):
    Carrier = 5
    Battleship = 4
    Destroyer = 3
    Submarine = 3
    PatrolBoat = 2

index = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
cols = ["A","B","C","D","E","F","G","H","I","J"]
horizontal = (True,False)

class BaseShip():
    def __init__(self, size, start, stop,isComputer):
        self.mSize = size
        self.mName = "S"
        if isComputer:
            self.randomPosition()
        else:
            self.setInputs(start,stop)

    def setInputs(self,start,stop):
            self.mStart = (cols.index(start[0]), int(start[1]))
            self.mStop = (cols.index(stop[0]), int(stop[1]))

    def __str__(self):
        return str(self.mStart) +"," + str(self.mStop)

    def position(self):
        return self.mStart, self.mStop

    def name(self):
        return self.mName

    def randomPosition(self):
        isHorizontal = random.choice(horizontal)
        p1, p2 = 0, 0
        column = random.choice(index)
        while(self.mSize != (abs(p1-p2)+1)):
            p1 = random.choice(index)
            p2 = random.choice(index)

        if isHorizontal:
            if p1 > p2:
                p1,p2 = p2,p1
            self.mStart = (column, p1)
            self.mStop = (column, p2)
        else:
            startPos = p1 if p1 < p2 else p2
            self.mStart =  (startPos, p1)
            self.mStop =  (startPos+self.mSize-1, p1)

# class Carrier(BaseShip): //Tek değişiklik size olduğu için ayırmaya gerek kalmadı!
#     def __init__(self, start,stop,random=False):
#         super(Carrier,self).__init__(AllShips.Carrier.value,start,stop,random)
#
# class BattleShip(BaseShip):
#     def __init__(self, start, stop,random=False):
#         super(BattleShip,self).__init__(AllShips.Battleship.value,start,stop,random)
#
# class Destroyer(BaseShip):
#     def __init__(self, start,stop,random=False):
#         super(Destroyer,self).__init__(AllShips.Destroyer.value,start,stop,random)
#
# class Submarine(BaseShip):
#     def __init__(self, start, stop,random=False):
#         super(Submarine,self).__init__(AllShips.Submarine.value,start,stop,random)
#
# class PatrolBoat(BaseShip):
#     def __init__(self, start, stop,random=False):
#         super(PatrolBoat,self).__init__(AllShips.PatrolBoat.value,start,stop,random)
