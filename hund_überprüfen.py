import Daten_Antworten
import hunderassen

antwort = Daten_Antworten.Antworten_liste

Labrador = hunderassen.Labrador
Französische_Bulldogge = hunderassen.Französische_Bulldogge
Chihuahua = hunderassen.Chihuahua
Golden_Retriever = hunderassen.Golden_Retriever
Australian_Shepherd = hunderassen.Australian_Shepherd
Jack_Russel = hunderassen.Jack_Russel
Deutscher_Schäferhund = hunderassen.Deutscher_Schäferhund
Havaneser = hunderassen.Havaneser
Yorkshire_Terrier = hunderassen.Yorkshire_Terrier
Malteser = hunderassen.Malteser
Border_Collie = hunderassen.Border_Collie
Mops = hunderassen.Mops
Beagle = hunderassen.Beagle
Rhodesian_Ridgeback = hunderassen.Rhodesian_Ridgeback
Berner_Sennenhund = hunderassen.Berner_Sennenhund
Dackel = hunderassen.Dackel
Rottweiler = hunderassen.Rottweiler
Dobermann = hunderassen.Dobermann
Zwergspitz = hunderassen.Zwergspitz
Boxer = hunderassen.Boxer



def hundueberpruefen():
    if antwort == Labrador:
        hund = 'Labrador'

    elif antwort == Französische_Bulldogge:
        hund = 'Französische Bulldogge'

    elif antwort == Chihuahua:
        hund = 'Chihuahua'
    else:
        hund = 'probier es noch einmal'
    antwort.clear()

'''
def hundueberpruefen():
    if len(antwortenquiz) == len(Labrador) and len(antwortenquiz) == sum(
            [1 for i, j in zip(antwortenquiz, Labrador) if i == j]):
        print("The lists are identical")
    else:
        print("The lists are not identical")
'''
