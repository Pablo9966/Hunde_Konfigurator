import json

def antwortspeichern(datei, frage):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[frage] = frage

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)
