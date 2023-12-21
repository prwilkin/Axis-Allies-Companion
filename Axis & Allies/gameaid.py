income_data = {}
territory_data = {}
turn_number = 0
phase = 'error'


# game load functions
def load_game_data(filename):
    global income_data
    global territory_data
    global turn_number
    global phase

    with open(filename, 'r') as file:
        lines = file.readlines()

    # Process global data
    line = lines[2]
    turn_number = line.split(": ")[1].strip()
    line = lines[3]
    phase = line.split(": ")[1].strip()

    for line in lines[4:13]:
        country, income = line.strip().split(': ')
        income_data[country] = income

    # Process territory data
    for line in lines[15:342]:
        continent_territory, country_ipc = line.strip().split(': ')
        continent, territory = continent_territory.split('/')
        country, ipc = country_ipc.split('/')
        if continent not in territory_data:
            territory_data[continent] = {}
        territory_data[continent][territory] = [country, ipc]
    return None


# game save function
def save_game_data(filename):
    global income_data
    global territory_data
    global turn_number
    global phase

    with open(filename, 'w') as file:
        # Write the Global Data header and the corresponding data
        file.write('Global Data\n')
        file.write('Turn: ' + str(turn_number) + '\n')
        file.write('Phase: ' + phase + '\n')
        for key, value in income_data.items():
            file.write(f'{key}: {value}\n')

        # Write the Territory Data header and the corresponding data
        file.write('Territory Data\n')
        for continent, territories in territory_data.items():
            for territory, country_ipc in territories.items():
                file.write(f'{continent}/{territory}: {country_ipc[0]}/{country_ipc[1]}\n')
    return None


# will move to next phase and turn
def next_phase():
    global phase
    if phase == 'France':
        phase = 'Germany'
        global turn_number
        turn_number += 1
        return
    elif phase == 'ANZAC':
        phase = 'France'
    elif phase == 'Italy':
        phase = 'ANZAC'
    elif phase == 'United Kingdom Pacific':
        phase = 'Italy'
    elif phase == 'United Kingdom Europe':
        phase = 'United Kingdom Pacific'
    elif phase == 'China':
        phase = 'United Kingdom Europe'
    elif phase == 'United States':
        phase = 'China'
    elif phase == 'Japan':
        phase = 'United States'
    elif phase == 'Soviet Union':
        phase = 'Japan'
    elif phase == 'Germany':
        phase = 'Soviet Union'
    return


# adjust IPC and territory ownership
def territory_take(continent, territory):
    global territory_data
    global phase

    income_data[territory_data[continent][territory][0]] -= territory_data[continent][territory][1]
    income_data[phase] += territory_data[continent][territory][1]
    territory_data[continent][territory][0] = phase
    return


# bonuses and convoys
