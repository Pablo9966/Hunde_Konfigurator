#hier definiere ich eine Liste, in welcher anschliessend die Antworten des Users abgespeichert werden
Antworten_liste = []

#hier ist der Algorithmus, welcher die Antwort in der Liste abspeichert. Dies wurde ausgegliedert, da so das main.py kürzer und übersichtlicher wird
def antwortensichern(antwort):
    Antworten_liste.append(antwort)

    return Antworten_liste
