# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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
        seazoneTable[territory] = str(newCountry)
        # TODO: seazone changes
    else:
        oldCountry, ipc = territoryTable[territory]
        ipcTable[oldCountry + 'Turn'] -= ipc
        ipcTable[newCountry + 'Turn'] += ipc
        territoryTable[territory] = newCountry


def color(country):
    country = str(country)
    if country == "ger":
        return "green"
    # TODO: add hex color values


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
    return


def saver(file):
    file = open(file)
    global turnNum, phase, countryTurn, ipcTable, bonusTable, territoryTable, seazoneTable
    # TODO: implement saving to file, add create a save file if one is not passed in
    return


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    loader("NewGame.txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
