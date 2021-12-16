import random

index = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
cols = ["A","B","C","D","E","F","G","H","I","J"]
move = {0:"_",1:"#",2:"*"}
maxScore = 17
class table():
    def __init__(self):
        self.tableList = {}
        self.mComputerMoveMemory = []
        self.tableList = {0:[],1:[],2:[], 3:[], 4:[],5:[], 6:[], 7:[],8:[],9:[] }
        for value in self.tableList.values():
            for i in range(1,11):
                value.append(move[0])

    def __str__(self):
        self.str = "  0 1 2 3 4 5 6 7 8 9\n"
        newLine = "\n"
        for key in self.tableList.keys():
            self.str += cols[key] + " "
            for i in range(10):
                self.str += (str(self.tableList[key][i])) + " "
            self.str += newLine
        return self.str

    def showComputerTable(self):
        self.str = "  0 1 2 3 4 5 6 7 8 9\n"
        newLine = "\n"
        for key in self.tableList.keys():
            self.str += cols[key] + " "
            for i in range(10):
                isHidden = self.tableList[key][i] if self.tableList[key][i] != "S" else move[0] # eğer gemi varsa gizle
                self.str += (isHidden) + " "
            self.str += newLine
        return self.str

    def placeShip(self,ship):
        start, stop = ship.position()
        for x in range(start[0],stop[0]+1):
            for y in range(start[1],stop[1]+1):
                if self.tableList[x][y] != move[0]:
                    # print("dolu denk geldi")
                    # print(self)
                    return False

        for x in range(start[0],stop[0]+1):
            for y in range(start[1],stop[1]+1):
                # print("yerleştirildi", ship.mName)
                self.tableList[x][y] = ship.name()
        return True

    def inputShipRandomly(self,ship):
        result = self.placeShip(ship)
        while not result:
            ship.randomPosition()
            result = self.placeShip(ship)
        # print(self)

    def move(self,position,isComputer):
        if len(position) != 2:
            print("Position type is wrong!")
            return False
        elif not (position[0].isalpha() and cols.count(position[0]) == 1 and position[1].isdigit() and index.count(int(position[1])) == 1) :
            print("Position type is not correct!")
            return False
        elif self.tableList[cols.index(position[0])][int(position[1])] == move[0]:
            self.tableList[cols.index(position[0])][int(position[1])] = move[1]
            if isComputer: print("Computer miss :)")
            else: print("You missed :(")
        elif self.tableList[cols.index(position[0])][int(position[1])] == move[1]:
            if isComputer: print("Computer attacked same!")
            else: print("Same place attack!")
        elif self.tableList[cols.index(position[0])][int(position[1])] == "S":
            self.tableList[cols.index(position[0])][int(position[1])] = move[2]
            if isComputer: print("Computer Hit :(")
            else : print("You Hit! :)")

    def randomMove(self):
        move = random.choice(self.mComputerMoveMemory)
        self.mComputerMoveMemory.remove(move)
        return move

    def setComputerMoves(self):
        for x in cols:
            for y in index:
                self.mComputerMoveMemory.append(x+str(y))

    def checkScore(self,isComputer):
        score = 0
        for value in self.tableList.values():
            for i in range(0,10):
                if value[i] == move[2]:
                    score += 1;
        whoPlays = "Computer's" if isComputer else "User's"
        print(whoPlays +" score: ", score)
        if score == maxScore:
            return True
        else:
            return False
