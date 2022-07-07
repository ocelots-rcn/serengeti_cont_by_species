import json
data = {'variables': ['Amount of Shade', 'Distance to Confluence (m)', 'Distance to Kopje (m)', 'Distance to River (m)', 'Greeness (Dry)', 'Greeness (Wet)', 'Lion Risk (Dry)', 'Lion Risk (Wet)', 'Tree Density Measure', 'Longitude (m)', 'Latitude (m)' ], 'species': {}}

f = open('S1-11_filtered.csv', 'r')
line = f.readline()
while True:
    line = f.readline()
    if not line:
        break
    parts = line.split(',')
    key = parts[6].lower()
    if key not in data['species']:
        data['species'][key] = {}
        for var in data['variables']:
            data['species'][key][var] = []
    try:
        data['species'][key]['Amount of Shade'].append(float(parts[18]))
    except ValueError:
        pass
    try:
        data['species'][key]['Distance to Confluence (m)'].append(float(parts[20]))
    except ValueError:
        pass
    try:
        data['species'][key]['Distance to Kopje (m)'].append(float(parts[21]))
    except ValueError:
        pass
    try:
        data['species'][key]['Distance to River (m)'].append(float(parts[19]))
    except ValueError:
        pass
    try:
        data['species'][key]['Greeness (Dry)'].append(float(parts[26]))
    except ValueError:
        pass
    try:
        data['species'][key]['Greeness (Wet)'].append(float(parts[25]))
    except ValueError:
        pass
    try:
        data['species'][key]['Lion Risk (Dry)'].append(float(parts[24]))
    except ValueError:
        pass
    try:
        data['species'][key]['Lion Risk (Wet)'].append(float(parts[23]))
    except ValueError:
        pass
    try:
        data['species'][key]['Tree Density Measure'].append(float(parts[22]))
    except ValueError:
        pass
    try:
        data['species'][key]['Longitude (m)'].append(int(parts[15]))
    except ValueError:
        pass
    try:
        data['species'][key]['Latitude (m)'].append(int(parts[16]))
    except ValueError:
        pass
f.close()
f = open('../S1-11_filtered.json', 'w')
json.dump(data, f)
f.close()
