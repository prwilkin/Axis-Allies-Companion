import unittest
from src.bonusCalculator import gerBonusCalc, ussrBonusCalc, originalAxis, berlin
from src.bonusCalculator import japBonusCalc, islandAxis, powerCitiesAxis, stratResourcesAxis
from src.bonusCalculator import usBonusCalc, mainlandUS, extendedUS, extendedUS2
from src.bonusCalculator import chinaBonusCalc, ukeurBonusCalc, ukpacBonusCalc
from src.bonusCalculator import itaBonusCalc, romanAxis, africaAxis, oilAxis
from src.bonusCalculator import anzacBonusCalc, malayaAlly, dutchAlly
from src.mainBackend import updateTerritory, loader
from src.mainBackend import territoryTable, bonusTable


class Germany_Bonuses(unittest.TestCase):
    def test_main(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        self.assertEqual(10, gerBonusCalc(), msg="Turn 1 = should be 10")

    def test_2ndblock(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        bonusTable["ussr-ger"] = True
        self.assertEqual(5, gerBonusCalc(), msg="At war with USSR = should be 5")
        x = ["Novgorod", "Volgograd", "Russia"]
        for territory in x:
            updateTerritory(territory, "ger")
        updateTerritory("Caucasus", "jap")
        self.assertEqual(25, gerBonusCalc(), msg="At war with USSR w/ territories = should be 25")

    def test_3rdblock(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        bonusTable["egypt"] = "ger"
        self.assertEqual(15, gerBonusCalc(), msg="Egypt under ger = should be 15")

    def test_4thblock(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        updateTerritory("Denmark", "us")
        self.assertEqual(5, gerBonusCalc(), msg="Should not get swed bonus = should be 5")
        updateTerritory("Denmark", "ger")
        self.assertEqual(10, gerBonusCalc(), msg="Gets swed bonus = should be 10")
        updateTerritory("Sweden", "pal")
        self.assertEqual(5, gerBonusCalc(), msg="Should not get swed bonus = should be 5")

    def test_5thblock(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        x = ["Iraq", "Persia", "Northwest Persia"]
        for territory in x:
            updateTerritory(territory, "ger")
        self.assertEqual(16, gerBonusCalc(), msg="Middle East = should be 16")

    # def test_something(self):
    #     self.assertTrue(False)  # add assertion here


class USSR_Bonuses(unittest.TestCase):
    def test_main(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        self.assertEqual(0, ussrBonusCalc(), msg="No war = should be 0")
        bonusTable["ussr-ita"] = True
        self.assertEqual(5, ussrBonusCalc(), msg="War = should be 5")

    def test_originalAxis(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        self.assertEqual(0, originalAxis(), msg="No owners = should be 0")
        x = ["Greater Southern Germany", "Holland Belgium", "Ethiopia", "Italian Somaliland",
             "Finland", "Bulgaria", "Iraq"]
        for territory in x:
            updateTerritory(territory, "ussr")
        self.assertEqual(21, originalAxis(), msg="8 owners = should be 24")
        bonusTable["ussr-ita"] = True
        self.assertEqual(26, ussrBonusCalc(), msg="War = should be 29")

    def test_berlin(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        bonusTable["ussr-ita"] = True
        berlin()
        self.assertEqual(0, bonusTable["berlin"], msg="No owner = should be 0")
        updateTerritory("Germany", "ussr")
        berlin()
        self.assertEqual(1, bonusTable["berlin"], msg="ussr new = should be 1")
        self.assertEqual(18, ussrBonusCalc(), msg="ussr berlin = should be 15")
        berlin()
        self.assertEqual(1, bonusTable["berlin"], msg="ussr still = should be 1")
        updateTerritory("Germany", "ita")
        berlin()
        self.assertEqual(2, bonusTable["berlin"], msg="ussr not owner = should be 2")
        self.assertEqual(5, ussrBonusCalc(), msg="ussr not owner = should be 5")


class Japan_Bonuses(unittest.TestCase):
    def test_main(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        self.assertEqual(10, japBonusCalc(), msg="No war = should be 10")
        bonusTable["unprovoked"] = True
        self.assertEqual(0, japBonusCalc(), msg="No war, edge case = should be")
        bonusTable["us-jap"] = True
        self.assertEqual(0, japBonusCalc(), msg="war no holdings = should be 0")

    def test_islandAxis(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        bonusTable["us-jap"] = True
        self.assertFalse(islandAxis(), msg="normal = should be False")
        x = ["Guam", "Midway", "Wake Island", "Gilbert Islands", "Solomon Islands"]
        for territory in x:
            updateTerritory(territory, "ita")
        self.assertTrue(islandAxis(), msg="All axis = should be True")
        self.assertEqual(5, japBonusCalc(), msg="Original axis =  should be 5")
        x = ["Guam", "Midway", "Wake Island", "Solomon Islands"]
        for territory in x:
            updateTerritory(territory, "jap")
        updateTerritory("Gilbert Islands", "us")
        self.assertFalse(islandAxis(), msg="Edge case = should be False")

    def test_powerCities(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        bonusTable["us-jap"] = True
        self.assertEqual(0, powerCitiesAxis(), msg="No control = should be 0")
        x = ["India", "New South Wales", "Hawaiian Islands", "Western United States"]
        for territory in x:
            updateTerritory(territory, "jap")
        self.assertEqual(20, powerCitiesAxis(), msg="All Axis = should be 20")
        self.assertEqual(20, japBonusCalc(), msg="powerCitiesAxis = should be 20")

    def test_strat(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        bonusTable["us-jap"] = True
        self.assertFalse(stratResourcesAxis(), msg="No control = should be False")
        x = ["Sumatra", "Java", "Borneo", "Celebes"]
        for territory in x:
            updateTerritory(territory, "jap")
        self.assertTrue(stratResourcesAxis(), msg="Full control = should be True")
        self.assertEqual(5, japBonusCalc(), msg="strat = should be 5")


class US_Bonuses(unittest.TestCase):
    def test_main(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        self.assertEqual(0, usBonusCalc(), msg="No war = should be 0")
        bonusTable["us-jap"] = True
        self.assertEqual(25, usBonusCalc(), msg="War = should be 25")
        bonusTable["usfra"] = True
        self.assertEqual(30, usBonusCalc(), msg="with troops in fra = should be 25")
        updateTerritory("Philippines", "jap")
        self.assertEqual(25, usBonusCalc(), msg="no Philippines = should be 25")

    def test_mainland(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        bonusTable["us-jap"] = True
        self.assertTrue(mainlandUS(), msg="Control = should be True")
        updateTerritory("Central United States", "jap")
        self.assertFalse(mainlandUS(), msg="One off = should be False")
        self.assertEqual(15, usBonusCalc(), msg="no mainland = should be 15")

    def test_extended(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        bonusTable["us-jap"] = True
        self.assertTrue(extendedUS(), msg="Control = should be True")
        updateTerritory("Hawaiian Islands", "jap")
        self.assertFalse(extendedUS(), msg="One off = should be False")
        self.assertEqual(20, usBonusCalc(), msg="no extended = should be 20")

    def test_extended2(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        bonusTable["us-jap"] = True
        self.assertTrue(extendedUS2(), msg="Control = should be True")
        updateTerritory("Central America", "jap")
        self.assertFalse(extendedUS2(), msg="One off = should be False")
        self.assertEqual(20, usBonusCalc(), msg="no extended2 = should be 20")


class China_Bonuses(unittest.TestCase):
    def test_main(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        self.assertEqual(6, chinaBonusCalc(), msg="Control = should be 6")
        updateTerritory("Burma", "jap")
        self.assertEqual(0, chinaBonusCalc(), msg="One off = should be 0")


class ukeur_Bonuses(unittest.TestCase):
    def test_main(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        self.assertEqual(5, ukeurBonusCalc(), msg="Control = should be 5")
        updateTerritory("Iceland", "ger")
        self.assertEqual(0, ukeurBonusCalc(), msg="One off = should be 0")


class ukpac_Bonuses(unittest.TestCase):
    def test_main(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        self.assertEqual(0, ukpacBonusCalc(), msg="Control = should be 0")
        bonusTable["uk/anzac-jap"] = True
        self.assertEqual(5, ukpacBonusCalc(), msg="War = should be 5")
        updateTerritory("Malaya", "jap")
        self.assertEqual(0, ukpacBonusCalc(), msg="One off = should be 0")


class Italy_Bonuses(unittest.TestCase):
    def test_main(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        self.assertEqual(0, itaBonusCalc(), msg="Control = should be 0")
        bonusTable["mediterranean"] = False
        self.assertEqual(5, itaBonusCalc(), msg="No ally warships = should be 5")

    def test_roman(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        self.assertFalse(romanAxis(), msg="Control = should be False")
        x = ["Gibraltar", "Southern France", "Greece", "Egypt"]
        for territory in x:
            updateTerritory(territory, "ger")
        self.assertTrue(romanAxis(), msg="All Axis = should be True")
        updateTerritory("Southern France", "ukeur")
        self.assertTrue(romanAxis(), msg="One off = should be True")
        self.assertEqual(5, itaBonusCalc(), msg="roman = should be 5")
        updateTerritory("Egypt", "ukeur")
        self.assertFalse(romanAxis(), msg="Two off = should be False")
        self.assertEqual(0, itaBonusCalc(), msg="roman = should be 0")

    def test_africa(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        self.assertFalse(africaAxis(), msg="Control = should be False")
        x = ["Morocco", "Algeria", "Tunisia", "Libya", "Tobruk", "Alexandria"]
        for territory in x:
            updateTerritory(territory, "ger")
        self.assertTrue(africaAxis(), msg="All Axis = should be True")
        self.assertEqual(5, itaBonusCalc(), msg="Africa = should be 5")

    def test_oil(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        self.assertEqual(0, oilAxis(), msg="Control = should be 0")
        x = ["Iraq", "Persia", "Northwest Persia"]
        for territory in x:
            updateTerritory(territory, "ita")
        self.assertEqual(6, oilAxis(), msg="All ita = should be 6")
        self.assertEqual(6, itaBonusCalc(), msg="oil = should be 6")


class Anzac_Bonuses(unittest.TestCase):
    def test_main(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        self.assertEqual(0, anzacBonusCalc(), msg="Control = should be 0")
        bonusTable["uk/anzac-jap"] = True
        self.assertEqual(5, anzacBonusCalc(), msg="War = should be 10")

    def test_malaya(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        self.assertTrue(malayaAlly(), msg="Control = should be True")
        updateTerritory("Malaya", "jap")
        self.assertFalse(malayaAlly(), msg="No Malaya = should be False")
        bonusTable["uk/anzac-jap"] = True
        self.assertEqual(0, anzacBonusCalc(), msg="malaya = should be 5")
        updateTerritory("Malaya", "anzac")
        updateTerritory("New Britain", "jap")
        self.assertFalse(malayaAlly(), msg="One off = should be False")

    def test_dutch(self):
        loader("C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/NewGame.txt")
        self.assertFalse(dutchAlly(), msg="Control = should be False")
        bonusTable["uk/anzac-jap"] = True
        self.assertEqual(5, anzacBonusCalc(), msg="malaya = should be 5")
        updateTerritory("New Britain", "jap")
        self.assertFalse(dutchAlly(), msg="One off = should be False")


if __name__ == '__main__':
    unittest.main()
