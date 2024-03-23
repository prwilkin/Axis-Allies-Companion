import tkinter as tk
from tkinter import filedialog
import os
# Owners: Germany, ger; USSR, ussr; Japan, jap; USA, us; China, china; UK-Europe, ukeur; UK-Pacific, ukpac;
# Italy, ita; ANZAC, anzac; France, fra, Neutral, nue; Pro-Ally, pal; Pro-Axis, pax;
#
# Bonus Table: ussr-ger, USSR & Germany at war; ussr-jap, USSR & Japan; ussr-ita, USSR & Italy at war;
# uk/anzac-jap, UK/ANZAC & Japan at war; us-jap, US & Japan at war; us-ger, US & Germany at war;
# egypt, if at least 1 German land unit in Axis controlled Egypt; seazone125, Sea Zone 125 free of axis warship
# allyussr, No allies in original USSR territory; berlin, number of times USSR controls Germany; indochina, Japan hasn't
# attacked French Indo China; unprovoked, Japan does not attack UK/ANZAC unprovoked; usfra, if at least 1 US land unit
# in France; mediterranean, Ally warships in the med;
#
# Colors: ger, #626362; ussr, #BB0000; jap, #FE4800; us, #186518; china, #FE4800; ukeur, #FAC807; ukpac, #987906;
# ita, #5E4220; anzac, #5B8684; fra, #2870BA; nue, #D1B883; pal, #FEEDC7; pax, #978762; seanue, #d9d9d9;


def convoyCountry(country):
    import src.header as header
    x = list()
    for territory in header.convoyTable.keys():
        val = header.convoyTable[territory]
        if val == country:
            x.append(territory)
    return x


def changeOwner(territory):
    from AandAQTCreatorUI.main import changeCountryWindow
    changeCountryWidget = changeCountryWindow()
    changeCountryWidget.territory(territory)
    changeCountryWidget.exec_()
    return changeCountryWidget.country


def updateTerritory(territory, newCountry):
    import src.header as header
    if "Sea Zone" in territory:
        header.seazoneTable[territory] = str(newCountry).lower()
        header.convoyTable[territory] = str(newCountry).lower()
    else:
        oldCountry, ipc = header.territoryTable[territory]
        # TODO: check for turn and war limits with extra functions
        if oldCountry not in ("nue", "pal", "pax"):
            header.ipcTable[oldCountry + 'Turn'] -= ipc
        if newCountry not in ("nue", "pal", "pax"):
            header.ipcTable[newCountry + 'Turn'] += ipc
        header.territoryTable[territory] = [str(newCountry).lower(), ipc]
    # print("Updated Territory")


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
    elif country == "nue":
        return "#D1B883"
    elif country == "pal":
        return "#FEEDC7"
    elif country == "pax":
        return "#978762"
    else:
        return None


def nextCountry(country):
    if country == "Germany":
        return "USSR"
    elif country == "USSR":
        return "Japan"
    elif country == "Japan":
        return "USA"
    elif country == "USA":
        return "China"
    elif country == "China":
        return "UK-Eur"
    elif country == "UK-Eur":
        return "UK-Pac"
    elif country == "UK-Pac":
        return "Italy"
    elif country == "Italy":
        return "ANZAC"
    elif country == "ANZAC":
        return "France"
    elif country == "France":
        import src.header as header
        header.turnNum += 1
        return "Germany"
    else:
        return None


def loader():
    # print("Loading data...")
    # parser(file)
    os.chdir("..")
    load_path = tk.filedialog.askopenfilename(initialdir=os.curdir + "/saves")   # prevents an empty tkinter window from appearing
    os.chdir("./AandAQTCreatorUI")
    parser(load_path)


def parser(file):
    file = open(file)
    # print("Begin parsing")
    import src.header as header
    i = 1
    for line in file:
        if i < 38:  # line 38 begins territory
            key, value = line.split(": ")
            value = value.strip()
            if i == 1:
                header.turnNum = int(value)
            elif i == 2:
                header.phase = str(value)
            elif i == 3:
                header.countryTurn = str(value)
            elif i <= 23:
                header.ipcTable.update({key: int(value)})
            elif i <= 36:
                if value == "False":
                    header.bonusTable.update({key: False})
                else:
                    header.bonusTable.update({key: True})
            elif i == 37:
                header.bonusTable.update({key: int(value)})
        else:
            territory, info = line.split(": ")
            if i <= 238:    # line 239 is seazone
                country, IPC = info.split("/")
                header.territoryTable.update({territory: [str(country), int(IPC)]})
            else:
                if info is None:
                    header.seazoneTable.update({territory: None})
                else:
                    header.seazoneTable.update({territory: str(info)})
                    header.convoyTable.update({territory: str(info)})
        i += 1
    # print("End parsing")
    return file.close()


def saver():
    os.chdir("..")
    save_path = tk.filedialog.asksaveasfile(mode='w', initialdir=os.curdir + "/saves", defaultextension=".txt")
    os.chdir("./AandAQTCreatorUI")
    import src.header as header
    save_path.write("turn: " + str(header.turnNum) + "\n")
    save_path.write("phase: " + str(header.phase) + "\n")
    save_path.write("country: " + str(header.countryTurn) + "\n")
    for x in header.ipcTable.keys():
        save_path.write(x + ': ' + str(header.ipcTable[x]) + "\n")
    for x in header.bonusTable.keys():
        save_path.write(x + ': ' + str(header.bonusTable[x]) + "\n")
    for x in header.territoryTable.keys():
        save_path.write(x + ': ' + str(header.territoryTable[x][0]) + '/' + str(header.territoryTable[x][1]) + "\n")
    for x in header.seazoneTable.keys():
        y = str(header.seazoneTable[x]).replace("\n", "")
        save_path.write(x + ': ' + y + "\n")
    return


if __name__ == '__main__':
    parser("NewGame.txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
