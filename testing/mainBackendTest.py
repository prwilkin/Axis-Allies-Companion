import unittest
from src.mainBackend import updateTerritory, colorPicker, loader
from src.mainBackend import ipcTable, territoryTable


class MyTestCase(unittest.TestCase):
    def test_updateTerritory(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        updateTerritory("Poland", "ita")
        self.assertEqual(12, ipcTable["itaTurn"], msg="Italy Turn IPC is not 12 = didn't add")
        self.assertEqual(38, ipcTable["gerTurn"], msg="Germany Turn IPC is not 38 = didnt subtract")
        updateTerritory("Poland", "ger")
        self.assertEqual(10, ipcTable["itaTurn"], msg="Italy Turn IPC is not 10 = didn't subtract")
        self.assertEqual(40, ipcTable["gerTurn"], msg="Germany Turn IPC is not 40 = didnt add")

    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
