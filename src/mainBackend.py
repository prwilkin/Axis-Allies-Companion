turnNum = 1
phase = "Purchase"      # Purchase, Combat, Income
countryTurn = "Germany" # Germany, USSR, Japan, USA, China, UK-Europe, UK-Pacific, Italy, ANZAC, France
ipcTable = {}           # IPC by countryBank & countryTurn keys, value is int*
bonusTable = {}         # Bonuses name as key, value is Bool* or int* (basically all the same)
territoryTable = {}     # Territory as key, value 0 is string* country controlling & value 1 is ipc int*
seazoneTable = {}       # Seazone as key, value is string* country or None
convoyTable = {}        # Seazone as key, value is string* country
# TODO: victory cities quick list
# TODO: Reference Table
# Owners: Germany, ger; USSR, ussr; Japan, jap; USA, us; China, china; UK-Europe, ukeur; UK-Pacific, ukpac;
# Italy, ita; ANZAC, anzac; France, fra, Neutral, nue; Pro-Ally, pal; Pro-Axis, pax;
#
# Bonus Table: ussr-ger, USSR & Germany at war; ussr-ita, USSR & Italy at war; ussr-jap, USSR & Japan;
# uk/anzac-jap, UK/ANZAC & Japan at war; us-jap, US & Japan at war; us-ger, US & Germany at war;
# egypt, if at least 1 German land unit in Axis controlled Egypt; seazone125, Sea Zone 125 free of axis warship
# allyussr, No allies in original USSR territory; berlin, number of times USSR controls Germany; indochina, Japan hasn't
# attacked French Indo China; unprovoked, Japan does not attack UK/ANZAC unprovoked; usfra, if at least 1 US land unit
# in France; mediterranean, Ally warships in the med;
#
# Colors: ger, #626362; ussr, #BB0000; jap, #FE4800; us, #186518; china, #FE4800; ukeur, #FAC807; ukpac, #987906;
# ita, #5E4220; anzac, #5B8684; fra, #2870BA;

# TODO: convoy logic needs to be added to detect the country


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
        # TODO: check for turn and war limits with extra functions
        if oldCountry not in ("nue", "pal", "pax"):
            ipcTable[oldCountry + 'Turn'] -= ipc
        if newCountry not in ("nue", "pal", "pax"):
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
    else:
        return None


# TODO: windows file manager, needs to be connected to the frontend load
def load():
    print("Loading data...")
    # parser(file)


# TODO: This is a parser, connect with windows File manager
def parser(file):
    file = open(file)
    print("Begin parsing")
    global turnNum, phase, countryTurn, ipcTable, bonusTable, territoryTable, seazoneTable
    i = 1
    for line in file:
        if i < 38:  # line 38 begins territory
            key, value = line.split(": ")
            value = value.strip()
            if i == 1:
                turnNum = int(value)
            elif i == 2:
                phase = str(value)
            elif i == 3:
                countryTurn = str(value)
            elif i <= 23:
                ipcTable.update({key: int(value)})
            elif i <= 36:
                if value == "False":
                    bonusTable.update({key: False})
                else:
                    bonusTable.update({key: True})
            elif i == 37:
                bonusTable.update({key: int(value)})
        else:
            territory, info = line.split(": ")
            if i <= 238:    # line 239 is seazone
                country, IPC = info.split("/")
                territoryTable.update({territory: [str(country), int(IPC)]})
            else:
                if info is None:
                    seazoneTable.update({territory: None})
                else:
                    seazoneTable.update({territory: str(info)})
                    convoyTable.update({territory: str(info)})
        i += 1
    print("End parsing")
    return file.close()


def saver(file):
    file = open(file)
    global turnNum, phase, countryTurn, ipcTable, bonusTable, territoryTable, seazoneTable
    # TODO: implement saving to file, add create a save file if one is not passed in
    return


if __name__ == '__main__':
    parser("NewGame.txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
