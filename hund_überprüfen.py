import Daten_Antworten
import csv
import _json

'''
csvFilePath = 'Hunderassen1.csv'
jsonFilePath = 'hunderassen.json'

data = {}

with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['id']
        data[id] = rows

with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))
'''

'''
with open('Hunderassen1.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('Hunderassen1.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[20] for rows in reader}
        print(mydict)
'''

with open('Hunderassen1.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)