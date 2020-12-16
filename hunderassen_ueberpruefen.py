import json
import Daten_Antworten

#hier hole ich die Antworten um die Rangordnung erstellen zu können
antworten = Daten_Antworten.Antworten_liste

#hier hole ich die hunderassen um die rangordnung erstellen zu können
daten = open("hunderassen.json")
hunderassen_1 = json.load(daten)

#hier erstelle ich das dictionary in dem die rangordnung erstellt werden soll
rangordnung_hunderassen_ueberpruefen = {}

#hier überprüfe ich den jeweiligen Hund. Aus dem main.py wird die Hunderassen mitgegeben und hier mittels einer Funktion auf den Rang überprüft und den Rang in ein Dict geladen
def hunderassenueberpruefen(hund):
    result = [i for i, j in zip(hunderassen_1[hund], antworten) if i == j]
    rang = len(result)
    rangordnung_hunderassen_ueberpruefen[hund] = rang

    return rangordnung_hunderassen_ueberpruefen