import unittest
from Table import table
from Ship import BaseShip

blankTable = "  0 1 2 3 4 5 6 7 8 9\n" \
             "A _ _ _ _ _ _ _ _ _ _ \n" \
             "B _ _ _ _ _ _ _ _ _ _ \n" \
             "C _ _ _ _ _ _ _ _ _ _ \n" \
             "D _ _ _ _ _ _ _ _ _ _ \n" \
             "E _ _ _ _ _ _ _ _ _ _ \n" \
             "F _ _ _ _ _ _ _ _ _ _ \n" \
             "G _ _ _ _ _ _ _ _ _ _ \n" \
             "H _ _ _ _ _ _ _ _ _ _ \n" \
             "I _ _ _ _ _ _ _ _ _ _ \n" \
             "J _ _ _ _ _ _ _ _ _ _ \n"

shipTable = "  0 1 2 3 4 5 6 7 8 9\n" \
             "A S S S S S _ _ _ _ _ \n" \
             "B _ _ _ _ _ _ _ _ _ _ \n" \
             "C _ _ _ _ _ _ _ _ _ _ \n" \
             "D _ _ _ _ _ _ _ _ _ _ \n" \
             "E _ _ _ _ _ _ _ _ _ _ \n" \
             "F _ _ _ _ _ _ _ _ _ _ \n" \
             "G _ _ _ _ _ _ _ _ _ _ \n" \
             "H _ _ _ _ _ _ _ _ _ _ \n" \
             "I _ _ _ _ _ _ _ _ _ _ \n" \
             "J _ _ _ _ _ _ _ _ _ _ \n"

computerHitTable = "  0 1 2 3 4 5 6 7 8 9\n" \
             "A * _ _ _ _ _ _ _ _ _ \n" \
             "B _ _ _ _ _ _ _ _ _ _ \n" \
             "C _ _ _ _ _ _ _ _ _ _ \n" \
             "D _ _ _ _ _ _ _ _ _ _ \n" \
             "E _ _ _ _ _ _ _ _ _ _ \n" \
             "F _ _ _ _ _ _ _ _ _ _ \n" \
             "G _ _ _ _ _ _ _ _ _ _ \n" \
             "H _ _ _ _ _ _ _ _ _ _ \n" \
             "I _ _ _ _ _ _ _ _ _ _ \n" \
             "J _ _ _ _ _ _ _ _ _ _ \n"

testShip = BaseShip(5,"A0","A4",False) # Carrier size ship = 5

class TestTable(unittest.TestCase):
    def setUp(self):
        self.meTable = table()

    def test_str(self):
        self.assertEqual(self.meTable.__str__(), blankTable, "Dogrusu: \n"+ blankTable)

    def test_placeShip(self):
        self.meTable.placeShip(testShip)
        self.assertEqual(self.meTable.__str__(),shipTable, "Dogrusu: \n"+ shipTable)

    def test_filledPositionShip(self):
        self.assertTrue(self.meTable.placeShip(testShip),msg="Önceden bu bölge doldurulduğu için doğrusu: False")

    def test_move(self):
        self.assertFalse(self.meTable.move("A15",False),msg="Fazla karakter girdisi girildi doğrusu: False")
        self.assertFalse(self.meTable.move("1B",False),msg="Ters bir pozisyon girildi doğrusu: False")
        self.meTable.placeShip(testShip)
        self.assertIsNone(self.meTable.move("A1",True), msg="User doğru oynayınca return doğrusu : None")
        self.assertIsNone(self.meTable.move("A0",False), msg="Computer User doğru oynayınca return doğrusu : None")

    def test_showComputerTable(self):
        self.meTable.placeShip(testShip)
        self.meTable.move("A0",False)
        self.assertEqual(self.meTable.showComputerTable().__str__(),computerHitTable,"Doğrusu: \n"+ computerHitTable)

    def test_randomMove(self):
        self.meTable.setComputerMoves()
        retVal = self.meTable.randomMove()
        self.assertFalse(self.meTable.mComputerMoveMemory.__contains__(retVal), msg="Computer attack sonrası yapılan "
                                                                                    "attack hafızadan silinmeli, doğrusu: False")
    def test_setComputerMoves(self):
        self.meTable.setComputerMoves()
        self.assertFalse(len(self.meTable.mComputerMoveMemory) < 1, msg = "Computer move'lar eklendikten sonra size artmalı "
                                                                          "doğrusu : False")

    def test_checkScore(self):
        self.meTable.placeShip(testShip)
        self.meTable.move("A0", False)
        self.assertFalse(self.meTable.checkScore(False), msg= "Tek bir atış yapıldığı için doğrusu : False")

    def tearDown(self):
        pass

class TestShip(unittest.TestCase):
    def setUp(self):
        self.meShip = BaseShip(3,"A1","A2",False)

    def test_position(self):
        self.meShip.setInputs("A1","A3")
        self.assertEqual(self.meShip.position(),((0, 1), (0, 3)),"Doğrusu: (0, 1), (0, 3) ")

    def test_name(self):
        self.assertEqual(self.meShip.name(), "S", "Doğrusu: 'S' ")

    def test_horizontal(self):
        isHorizontal = self.meShip.randomPosition()
        if isHorizontal: #  horizontal ise columnlar eşit değilse rowlar
            self.assertEqual(self.meShip.position()[0][0],self.meShip.position()[0][0],
                             "Dogrusu ikisininde :"+str(self.meShip.position()[0][0]))
        else:
            self.assertEqual(self.meShip.position()[0][1], self.meShip.position()[0][1],
                             "Dogrusu ikisininde"+str(self.meShip.position()[0][1]))

def suiteTable():
    my_suite = unittest.TestSuite()
    my_suite.addTest(TestTable('test_str'))
    my_suite.addTest(TestTable('test_placeShip'))
    my_suite.addTest(TestTable('test_filledPositionShip'))
    my_suite.addTest(TestTable('test_showComputerTable'))
    my_suite.addTest(TestTable('test_inputShipRandomly'))
    my_suite.addTest(TestTable('test_move'))
    my_suite.addTest(TestTable('test_randomMove'))
    my_suite.addTest(TestTable('test_setComputerMoves'))
    my_suite.addTest(TestTable('test_checkScore'))
    return my_suite

def suiteShip():
    my_suite = unittest.TestSuite()
    my_suite.addTest(TestShip('test_position'))
    my_suite.addTest(TestShip('test_name'))
    my_suite.addTest(TestShip('test_horizontal'))
    return my_suite

def run_tests():
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suiteShip())
    runner.run(suiteTable())

if __name__ == '__main__':
    unittest.main()
