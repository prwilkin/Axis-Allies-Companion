mainWin = None          # Main Window instance for App
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
# Bonus Table: ussr-ger, USSR & Germany at war; ussr-jap, USSR & Japan; ussr-ita, USSR & Italy at war;
# uk/anzac-jap, UK/ANZAC & Japan at war; us-jap, US & Japan at war; us-ger, US & Germany at war;
# egypt, if at least 1 German land unit in Axis controlled Egypt; seazone125, Sea Zone 125 free of axis warship
# allyussr, No allies in original USSR territory; berlin, number of times USSR controls Germany; indochina, Japan hasn't
# attacked French Indo China; unprovoked, Japan does not attack UK/ANZAC unprovoked; usfra, if at least 1 US land unit
# in France; mediterranean, Ally warships in the med;
#
# Colors: ger, #626362; ussr, #BB0000; jap, #FE4800; us, #186518; china, #FE4800; ukeur, #FAC807; ukpac, #987906;
# ita, #5E4220; anzac, #5B8684; fra, #2870BA; nue, #D1B883; pal, #FEEDC7; pax, #978762; seanue, #d9d9d9;
