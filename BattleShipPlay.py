import random

from Table import table
from Ship import BaseShip

# from Ship import Carrier
# from Ship import BattleShip
# from Ship import Destroyer
# from Ship import Submarine
# from Ship import PatrolBoat

isComputerStarter = (True,False)
index = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
cols = ["A","B","C","D","E","F","G","H","I","J"]
ships = {"Carrier":5,"Battleship":4,"Destroyer":3,"Submarine":3,"Patrolboat":2}

def setComputerShips(computer):
    for value in ships.values():
        ship = BaseShip(value,"","",True)
        computer.inputShipRandomly(ship)
    computer.setComputerMoves()
    # print(computer)

def setUserTable(table):
    for key in ships.keys():
        askPosition(key,ships[key],table)


def askPosition(shipName,size,table):
    userInput = input("Please enter "+ shipName +" ship start and stop position like 'A0 A"+str(size-1)+"': ")
    retVal = checkPosition(size,userInput);
    while retVal != True:
        userInput = input("Please enter like 'A0 A"+str(size-1)+"': ")
        retVal = checkPosition(size,userInput);
    ship = BaseShip(size,userInput.split()[0],userInput.split()[1],False)
    if not table.placeShip(ship):
        print("There is another ship entered coordinates!")
        askPosition(shipName,size,table)
    else:
        print(table)

def checkPosition(size,input):
    if len(input.split()) != 2:
        print("Input type is not correct!")
        return False

    start,stop = input.split()[0], input.split()[1]
    if len(start) != 2 or len(stop) != 2:
        print("Input size is not correct!")
    elif not (start[0].isalpha() and cols.count(start[0]) == 1 and start[1].isdigit() and index.count(int(start[1])) == 1
              and cols.count(stop[0]) == 1 and index.count(int(stop[1])) == 1):  # birinci değer kontrol A,B,C,D ikinci değer kotrol 1 2 3 4
        print("Input type is not correct!")
    elif start[0] == stop[0] and (size != (int(stop[1]) - int(start[1]) + 1)):
        print("This ship is " + str(size) + " hole sized, your input size is: " + str(int(stop[1]) - int(start[1]) + 1))
    elif start[1] == stop[1] and (size != (cols.index(stop[0]) - cols.index(start[0]) + 1)):
        print("This ship is " + str(size) + " hole sized, your input size is: " +
              str(cols.index(stop[0]) - cols.index(start[0]) + 1))
    else:
        return True

def play():
    computer = table()
    setComputerShips(computer)
    user = table()
    print("Welcome BattleShip game, your table is ready to set your ships")
    setUserTable(user)
    print("Your table is ready:\n", user)

    compStarter = random.choice(isComputerStarter)
    hasComputerWon = computer.checkScore(True)
    hasUserWon = user.checkScore(False)

    if compStarter:
        attack =  computer.randomMove()
        print("Computer has first move and attacked: ",attack)
        user.move(attack,True)
        print(user)

    while (hasComputerWon == False and hasUserWon == False):
        userAttack = input("Please enter attack place, like 'A0': ")
        attackResult = computer.move(userAttack,False)
        while attackResult == True:
            userAttack = input("Please enter attack place, like 'A0': ")
            attackResult = computer.move(userAttack, False)

        user.move(computer.randomMove(),True)
        # print(user)
        print(computer.showComputerTable())
        hasComputerWon = user.checkScore(True)
        hasUserWon = computer.checkScore(False)

    if hasComputerWon:
        print("Sorry computer has won maybe next time, good bye")
    else:
        print("Congrats you won! good bye")

play()
