from mainBackend import turnNum, ipcTable, bonusTable, territoryTable, seazoneTable, convoyTable


# Germany Bonuses
def gerBonusCalc():
    ipc = 0
    if not bonusTable["ussr-ger"]:  # not at war w/ ussr
        ipc += 5
    else:       # at war w/ ussr
        owner, x = territoryTable["Novgorod"]
        if owner == "ger":
            ipc += 5
        owner, x = territoryTable["Volgograd"]
        if owner == "ger":
            ipc += 5
        owner, x = territoryTable["Russia"]
        if owner == "ger":
            ipc += 5
        owner, x = territoryTable["Caucasus"]
        if owner == ("ger" or "ita" or "jap"):
            ipc += 5
    # when at war w/ us & fra   ~this is always the case though? not sure on instruction book format suggest dif
    if bonusTable["egypt"]:
        ipc += 5
    owner, x = territoryTable["Denmark"]
    if owner == "ger":      # ger control Denmark & Norway while Sweden is not pal or ally control
        owner, x = territoryTable["Norway"]
        if owner == "ger":
            owner, x = territoryTable["Sweden"]
            if owner == ("ussr" or "us" or "china" or "ukeur" or "ukpac" or "anzac" or "fra" or "pal"):
                ipc += 5
    owner, x = territoryTable["Iraq"]
    if owner == "ger":
        ipc += 2
    owner, x = territoryTable["Persia"]
    if owner == "ger":
        ipc += 2
    owner, x = territoryTable["Northwest Persia"]
    if owner == "ger":
        ipc += 2
    return ipc


# USSR Bonuses
def ussrBonusCalc():
    ipc = 0
    if bonusTable["ussr-ger"] or bonusTable["ussr-ita"]: # must be at war with ger or ita
        if bonusTable["seazone125"]:        # seazone125 no axis warship
            owner, x = territoryTable["Archangel"]
            if bonusTable["allyussr"] and (owner == "ussr"):    # Archangle owned by ussr and no land units in original soviet land
                ipc += 5
        ipc += originalAxis()  # +3 ipc for every ussr owned ger, ita, or pax territory
        berlin()    # first time ussr controls Germany (Berlin)
        if bonusTable["berlin"] == 1:
            ipc += 10
    return ipc


def originalAxis():
    ipc = 0
    axis = ["Denmark", "Germany", "Greater Southern Germany", "Holland Belgium", "Norway", "Poland", "Romania", "Slovakia Hungary",
            "Western Germany", "Ethiopia", "Italian Somaliland", "Libya", "Tobruk", "Albania", "Northern Italy", "Sardinia", "Sicily",
            "Southern Italy", "Finland", "Bulgaria", "Iraq"]
    for territory in axis:
        owner, x = territoryTable[territory]
        if owner == "ussr":
            ipc += 3
    return ipc


def berlin():
    x = bonusTable["berlin"]
    if x < 2:
        owner, x = territoryTable["Germany"]
        if (owner == "ger") and (x == 1):
            bonusTable["berlin"] = 2
        elif (owner == "ussr") and (x == 0):
            bonusTable["berlin"] = 1


# Japan Bonuses
def japBonusCalc():
    ipc = 0
    if not bonusTable["us-jap"] and not bonusTable["indochina"] and not bonusTable["unprovoked"]:
        ipc += 10       # No war with Anzac/uk, us, or french indo
    if bonusTable["us-jap"] or bonusTable["indochina"] or bonusTable["uk/anzac-jap"]:
        if islandAxis():        # if axis control 5 specific islands
            ipc += 5
        ipc += powerCitiesAxis()  # if axis control vic cities in pac
        if stratResourcesAxis():
            ipc += 5
    return ipc

def islandAxis():
    islands = ["Guam", "Midway", "Wake Island", "Gilbert Islands", "Solomon Islands"]
    allAxis = True
    for island in islands:
        owner, x = territoryTable[island]
        if owner != ("ger" or "ita" or "jap"):
            allAxis = False
    return allAxis


def powerCitiesAxis():
    ipc = 0
    cities = ["India", "New South Wales", "Hawaiian Islands", "Western United States"]
    for territory in cities:
        owner, x = territoryTable[territory]
        if owner != ("ger" or "ita" or "jap"):
            ipc += 5
    return ipc


def stratResourcesAxis():
    territories = ["Sumatra", "Java", "Borneo", "Celebes"]
    allAxis = True
    for territory in territories:
        owner, x = territoryTable[territory]
        if owner != ("ger" or "ita" or "jap"):
            allAxis = False
    return allAxis


# US Bonuses
def usBonusCalc():
    ipc = 0
    if bonusTable["us-jap"] or bonusTable["us-ger"]:
        if mainlandUS():
            ipc += 10
        if extendedUS():
            ipc += 5
        if extendedUS2():
            ipc += 5
        owner, x = territoryTable["Philippines"]
        if owner == "us":
            ipc += 5
        if bonusTable["usfra"]:
            ipc += 5
    return ipc


def mainlandUS():
    territories = ["Eastern United States", "Central United States", " Western United States"]
    allUS = True
    for territory in territories:
        owner, x = territoryTable[territory]
        if owner != "us":
            allUS = False
    return allUS


def extendedUS():
    territories = ["Alaska", "Aleutian Islands", "Hawaiian Islands", "Johnston Island", "Line Islands"]
    allUS = True
    for territory in territories:
        owner, x = territoryTable[territory]
        if owner != "us":
            allUS = False
    return allUS


def extendedUS2():
    territories = ["Mexico", "Southeast Mexico", "Central America", "West Indies"]
    allUS = True
    for territory in territories:
        owner, x = territoryTable[territory]
        if owner != "us":
            allUS = False
    return allUS


# China Bonuses
def chinaBonusCalc():
    ipc = 0
    territories = ["India", "Burma", "Yunnan", "Szechwan"]
    allAlly = True
    for territory in territories:
        owner, x = territoryTable[territory]
        if owner == ("ger" or "ita" or "jap"):
            allAlly = False
    if allAlly:
        ipc += 6
    return ipc


# UK Europe Economy
def ukeurBonusCalc():
    ipc = 0
    territories = ["Alexandria", "Anglo-Egyptian Sudan", "Belgian Congo", "British Somaliland", "Egypt", "Gold Coast",
                   "Kenya", "Nigeria", "Rhodesia", "South West Africa", "Tanganyika Territory", "Union of South Africa",
                   "Cyprus", "Gibraltar", "Iceland", "Malta", "Scotland", "United Kingdom", "Trans-Jordan",
                   "Alberta Saskatchewan Manitoba", "Western Canada", "New Brunswick Nova Scotia", "Newfoundland Labrador",
                   "Ontario", "Quebec", "British Guiana"]
    allUK = True
    for territory in territories:
        owner, x = territoryTable[territory]
        if owner != "ukeur":
            allUK = False
    if allUK:
        ipc += 5
    return ipc


# UK Pacific Economy
def ukpacBonusCalc():
    ipc = 0
    if bonusTable["uk/anzac-jap"]:
        owner, x = territoryTable["Kwangtung"]
        owner2, x = territoryTable["Malaya"]
        if (owner and owner2) == "ukpac":
            ipc += 5
    return ipc


# Italy Bonuses
def itaBonusCalc():
    ipc = 0
    if not bonusTable["mediterranean"]:
        ipc += 5
    if romanAxis():
        ipc += 5
    if africaAxis():
        ipc += 5
    ipc += oilAxis()
    return ipc


def romanAxis():
    territories = ["Gibraltar", "Southern France", "Greece", "Egypt"]
    allAxis = 0
    for territory in territories:
        owner, x = territoryTable[territory]
        if owner != ("ger" or "ita" or "jap"):
            allAxis += 1
    if allAxis <= 3:
        return True
    else:
        return False


def africaAxis():
    territories = ["Morocco", "Algeria", "Tunisia", "Libya", "Tobruk", "Alexandria"]
    allAxis = True
    for territory in territories:
        owner, x = territoryTable[territory]
        if owner != ("ger" or "ita" or "jap"):
            allAxis = False
    return allAxis


def oilAxis():
    ipc = 0
    territories = ["Iraq", "Persia", "Northwest Persia"]
    for territory in territories:
        owner, x = territoryTable[territory]
        if owner == "ita":
            ipc += 2
    return ipc


# ANZAC Bonuses
def anzacBonusCalc():
    ipc = 0
    if bonusTable["uk/anzac-jap"]:
        if malayaAlly():
            ipc += 5
        if dutchAlly():
            ipc += 5
    return ipc


def malayaAlly():
    territories = ["Malaya", "New South Wales", "Northern Territory", "Queensland", "South Australia", "Victoria",
                   "Western Australia", "New Britain", "New Guinea", "New Zealand", "Solomon Islands"]
    allAlly = True
    for territory in territories:
        owner, x = territoryTable[territory]
        if territory == "Malaya":
            if owner == ("ger" or "ita" or "jap"):
                return False
        else:
            if owner != "anzac":
                allAlly = False
    return allAlly


def dutchAlly():
    territories = ["Dutch New Guinea", "New Guinea", "New Britain", "Solomon Islands"]
    allAlly = True
    for territory in territories:
        owner, x = territoryTable[territory]
        if owner == ("ger" or "ita" or "jap" or "nue"):     # Dutch are not playable and thus labeled as nue for simplicity
            allAlly = False
    return allAlly


# France Bonuses
# there are none, damn it this game is so complex I do not want to go and write tests for bonuses
