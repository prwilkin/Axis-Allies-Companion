import unittest
from src.mainBackend import updateTerritory, colorPicker, parser
from src.mainBackend import ipcTable, territoryTable
import os


class MyTestCase(unittest.TestCase):
    def test_updateTerritory(self):
        os.chdir("..")
        parser(os.path.abspath(os.curdir) + "/src/NewGame.txt")
        updateTerritory("Poland", "ita")
        self.assertEqual(12, ipcTable["itaTurn"], msg="Italy Turn IPC is not 12 = didn't add")
        self.assertEqual(38, ipcTable["gerTurn"], msg="Germany Turn IPC is not 38 = didnt subtract")
        result1, result2 = territoryTable["Poland"]
        self.assertEqual("ita", result1, msg="territoryTable not correct = not updating")
        updateTerritory("Poland", "ger")
        self.assertEqual(10, ipcTable["itaTurn"], msg="Italy Turn IPC is not 10 = didn't subtract")
        self.assertEqual(40, ipcTable["gerTurn"], msg="Germany Turn IPC is not 40 = didnt add")
        result1, result2 = territoryTable["Poland"]
        self.assertEqual("ger", result1, msg="territoryTable not correct = not updating")
        # TODO: test seazone func

    def test_colorPicker(self):
        os.chdir("..")
        parser(os.path.abspath(os.curdir) + "/src/NewGame.txt")
        result = colorPicker("ita")
        self.assertEqual("#5E4220", result, msg="Ideal circumstances = wrong color")
        result = colorPicker("GER")
        self.assertEqual("#626362", result, msg="Malformed input = no error correction")
        result = colorPicker("Foo")
        self.assertEqual(None, result, msg="None valid input = didnt return None*")
        result = colorPicker("ukpac")
        self.assertEqual("#987906", result, msg="ukpac can be found after ukeur = no issue with == string* comparison")

    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
