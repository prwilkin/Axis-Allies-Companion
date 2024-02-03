import unittest

turnNum = 1
phase = "Purchase"      # Purchase, Combat, Income
countryTurn = "Germany" # Germany, USSR, Japan, USA, China, UK-Europe, UK-Pacific, Italy, ANZAC, France
ipcTable = {}           # IPC by countryBank & countryTurn keys, value is int*
bonusTable = {}         # Bonuses name as key, value is Bool*
territoryTable = {}     # Territory as key, value 0 is string* country controlling & value 1 is ipc int*
seazoneTable = {}       # Seazone as key, value is string* country or None
# TODO: fast list for convoys, look up rules


def changeOwner(territory):
    from AandAQTCreatorUI.main import changeCountryWindow
    changeCountryWidget = changeCountryWindow()
    changeCountryWidget.territory(territory)
    changeCountryWidget.exec_()
    return changeCountryWidget.country


def updateTerritory(territory, newCountry):
    global ipcTable, territoryTable, seazoneTable
    if "Sea Zone" in territory:
        seazoneTable[territory] = str(newCountry).lower()
        # TODO: seazone changes
    else:
        oldCountry, ipc = territoryTable[territory]
        ipcTable[oldCountry + 'Turn'] -= ipc
        ipcTable[newCountry + 'Turn'] += ipc
        territoryTable[territory] = [str(newCountry).lower(), ipc]


def colorPicker(country):
    country = str(country).lower()
    if country == "ger":
        return "#626362"
    elif country == "ussr":
        return "#BB0000"
    elif country == "jap":
        return "#FE4800"
    elif country == "us":
        return "#186518"
    elif country == "china":
        return "#FE4800"
    elif country == "ukeur":
        return "#FAC807"
    elif country == "ukpac":
        return "#987906"
    elif country == "ita":
        return "#5E4220"
    elif country == "anzac":
        return "#5B8684"
    elif country == "fra":
        return "#2870BA"
    # TODO: likely need neutrals


def loader(file):
    file = open(file)
    global turnNum, phase, countryTurn, ipcTable, bonusTable, territoryTable, seazoneTable
    i = 1
    for line in file:
        if i < 37:  # line 37 begins territory
            key, value = line.split(": ")
            if i == 1:
                turnNum = int(value)
            elif i == 2:
                phase = str(value)
            elif i == 3:
                countryTurn = str(value)
            elif i <= 23:
                ipcTable.update({key: int(value)})
            elif i <= 36:
                bonusTable.update({key: bool(value)})
        else:
            territory, info = line.split(": ")
            if i <= 237:    # line 238 is seazone
                country, IPC = info.split("/")
                territoryTable.update({territory: [str(country), int(IPC)]})
            else:
                seazoneTable.update({territory: lambda: None if info is None else str(info)})
        i += 1
    return file.close()


def saver(file):
    file = open(file)
    global turnNum, phase, countryTurn, ipcTable, bonusTable, territoryTable, seazoneTable
    # TODO: implement saving to file, add create a save file if one is not passed in
    return


if __name__ == '__main__':
    loader("NewGame.txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
