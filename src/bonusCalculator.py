from mainBackend import turnNum, ipcTable, bonusTable, territoryTable, seazoneTable


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


# TODO: entire bonus logic