import unittest
from src.bonusCalculator import gerBonusCalc
from src.mainBackend import updateTerritory, loader
from src.mainBackend import territoryTable, bonusTable


class Germany_Bonuses(unittest.TestCase):
    def test_main(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        self.assertEqual(10, gerBonusCalc(), msg="Turn 1 = should be 10")
        bonusTable["ussr-ger"] = True
        self.assertEqual(5, gerBonusCalc(), msg="At war with USSR = should be 5")
        x = ["Novgorod", "Volgograd", "Russia"]
        for territory in x:
            updateTerritory(territory, "ger")
        updateTerritory("Caucasus", "jap")
        self.assertEqual(25, gerBonusCalc(), msg="At war with USSR w/ territories = should be 25")

    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
