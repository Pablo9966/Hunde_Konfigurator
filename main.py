# zuerst importiere ich alle nötigen Funktionen und Dokumente
from flask import Flask
from flask import render_template
from flask import request
import Daten_Antworten
import hunderassen
import collections
import operator


app = Flask("Hunde Konfigurator")

# Hier hole ich die richtigen Antworten und speichere diese schön einfach als neue liste
antworten = Daten_Antworten.Antworten_liste

# hier erstelle ich die Rangliste der Hunde. Unten im Programm speichere ich hier die Anzahl Übereinstimmungen der Antworten des Users mit den vordefinierten Atributen der Hunde
rangordnung = {}

# hier starte ich die erste seite


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# hier starte ich die frage1. hier wird zudem die Antwort des Users mit dem Algorithmus antwortensichern aus der Datei Daten_Antworten in der Liste Antworten_Liste abgespeichert.


@app.route('/frage1', methods=['GET', 'POST'])
def frage1():
    if request.method == 'POST':
        antwort_frage1 = request.form['frage1']

        Daten_Antworten.antwortensichern(antwort_frage1)

    return render_template('frage1.html', frage1=frage1)


# hier starte ich die frage1. hier wird zudem die Antwort des Users mit dem Algorithmus antwortensichern aus der Datei Daten_Antworten in der Liste Antworten_Liste abgespeichert.
@app.route('/frage2', methods=['GET', 'POST'])
def frage2():
    if request.method == 'POST':
        antwort_frage2 = request.form['frage2']

        Daten_Antworten.antwortensichern(antwort_frage2)

    return render_template('frage2.html', frage2=frage2)


# hier starte ich die frage1. hier wird zudem die Antwort des Users mit dem Algorithmus antwortensichern aus der Datei Daten_Antworten in der Liste Antworten_Liste abgespeichert.
@app.route('/frage3', methods=['GET', 'POST'])
def frage3():
    if request.method == 'POST':
        antwort_frage3 = request.form['frage3']

        Daten_Antworten.antwortensichern(antwort_frage3)

    return render_template('frage3.html', frage3=frage3)


# hier starte ich die frage1. hier wird zudem die Antwort des Users mit dem Algorithmus antwortensichern aus der Datei Daten_Antworten in der Liste Antworten_Liste abgespeichert.
@app.route('/frage4', methods=['GET', 'POST'])
def frage4():
    if request.method == 'POST':
        antwort_frage4 = request.form['frage4']

        Daten_Antworten.antwortensichern(antwort_frage4)

    return render_template('frage4.html', frage4=frage4)


# hier starte ich die frage1. hier wird zudem die Antwort des Users mit dem Algorithmus antwortensichern aus der Datei Daten_Antworten in der Liste Antworten_Liste abgespeichert.
@app.route('/frage5', methods=['GET', 'POST'])
def frage5():
    if request.method == 'POST':
        antwort_frage5 = request.form['frage5']

        Daten_Antworten.antwortensichern(antwort_frage5)

    return render_template('frage5.html', frage5=frage5)


# hier starte ich die frage1. hier wird zudem die Antwort des Users mit dem Algorithmus antwortensichern aus der Datei Daten_Antworten in der Liste Antworten_Liste abgespeichert.
@app.route('/frage6', methods=['GET', 'POST'])
def frage6():
    if request.method == 'POST':
        antwort_frage6 = request.form['frage6']

        Daten_Antworten.antwortensichern(antwort_frage6)

    return render_template('frage6.html', frage6=frage6)


# hier wird die Antwort berechnet, die Reihenfolge bestimmt und dann die richtige Antwort herausgegeben
@app.route('/antwort')
def antwort():

    # Hier berechne ich jeweils die Anzahl Übereinstimmungen der Antworten des Users mit dem jeweiligen Hund. Anschliessend speichere ich diese Zahl im  zuvor definirten Dictionary ab. Dies wird für jeden Hund durchgeführt.
    # Labrador berechnen
    result_1 = [i for i, j in zip(hunderassen.Labrador, antworten) if i == j]
    rang_1 = len(result_1)
    rangordnung['Labrador'] = rang_1

# Französische Bulldogge brechnen
    result_2 = [i for i, j in zip(
        hunderassen.Französische_Bulldogge, antworten) if i == j]
    rang_2 = len(result_2)
    rangordnung['Französische Bulldogge'] = rang_2

# Chihuahua berechnen
    result_3 = [i for i, j in zip(hunderassen.Chihuahua, antworten) if i == j]
    rang_3 = len(result_3)
    rangordnung['Chihuahua'] = rang_3

# Golden Retriever berechnen
    result_4 = [i for i, j in zip(
        hunderassen.Golden_Retriever, antworten) if i == j]
    rang_4 = len(result_4)
    rangordnung['Golden Retriever'] = rang_4

# Australian Shepherd berechnen
    result_5 = [i for i, j in zip(
        hunderassen.Australian_Shepherd, antworten) if i == j]
    rang_5 = len(result_5)
    rangordnung['Australian Shepherd'] = rang_5

# Jack Russel berechnen
    result_6 = [i for i, j in zip(
        hunderassen.Jack_Russel, antworten) if i == j]
    rang_6 = len(result_6)
    rangordnung['Jack Russel'] = rang_6

# Deutscher Schäferhund berechnen
    result_7 = [i for i, j in zip(
        hunderassen.Deutscher_Schäferhund, antworten) if i == j]
    rang_7 = len(result_7)
    rangordnung['Deutscher Schäferhund'] = rang_7

# Havaneser berechnen
    result_8 = [i for i, j in zip(hunderassen.Havaneser, antworten) if i == j]
    rang_8 = len(result_8)
    rangordnung['Havaneser'] = rang_8

# Yorkshire Terrier berechnen
    result_9 = [i for i, j in zip(
        hunderassen.Yorkshire_Terrier, antworten) if i == j]
    rang_9 = len(result_9)
    rangordnung['Yorkshire Terrier'] = rang_9

# Malteser berechnen
    result_10 = [i for i, j in zip(hunderassen.Malteser, antworten) if i == j]
    rang_10 = len(result_10)
    rangordnung['Malteser'] = rang_10

# Border Collie berechnen
    result_11 = [i for i, j in zip(
        hunderassen.Border_Collie, antworten) if i == j]
    rang_11 = len(result_11)
    rangordnung['Border Collie'] = rang_11

# Mops berechnen
    result_12 = [i for i, j in zip(hunderassen.Mops, antworten) if i == j]
    rang_12 = len(result_12)
    rangordnung['Mops'] = rang_12

# Beagle berechnen
    result_13 = [i for i, j in zip(hunderassen.Beagle, antworten) if i == j]
    rang_13 = len(result_13)
    rangordnung['Beagle'] = rang_13

# Rhodesian Ridgeback berechnen
    result_14 = [i for i, j in zip(
        hunderassen.Rhodesian_Ridgeback, antworten) if i == j]
    rang_14 = len(result_14)
    rangordnung['Rhodesian Ridgeback'] = rang_14

# Berner Sennenhund berechnen
    result_15 = [i for i, j in zip(
        hunderassen.Berner_Sennenhund, antworten) if i == j]
    rang_15 = len(result_15)
    rangordnung['Berner Sennenhund'] = rang_15

# Dackel berechnen
    result_16 = [i for i, j in zip(hunderassen.Dackel, antworten) if i == j]
    rang_16 = len(result_16)
    rangordnung['Dackel'] = rang_16

# Rottweiler Berechnen
    result_17 = [i for i, j in zip(
        hunderassen.Rottweiler, antworten) if i == j]
    rang_17 = len(result_17)
    rangordnung['Rottweiler'] = rang_17

# Zwergspitz berechnen
    result_18 = [i for i, j in zip(
        hunderassen.Zwergspitz, antworten) if i == j]
    rang_18 = len(result_18)
    rangordnung['Zwergspitz'] = rang_18

# Boxer berechnen
    result_19 = [i for i, j in zip(hunderassen.Boxer, antworten) if i == j]
    rang_19 = len(result_19)
    rangordnung['Boxer'] = rang_19


# Hier ordne ich das Dictionary antworten nach der Anzahl Übereinstimmungen
    geordnete_rangordnung = collections.OrderedDict(
        sorted(rangordnung.items(), key=operator.itemgetter(1), reverse=True))

# Hier hole ich die Anzahl Übereinstimmungen hervor
    anzahl_uebereinstimmungen = geordnete_rangordnung.values()

    return render_template('antwort.html', rangordnung=rangordnung, geordnete_rangordnung=geordnete_rangordnung, anzahl_uebereinstimmungen=anzahl_uebereinstimmungen, zip=zip)

#Hier soll die Antworten_Liste gelöscht werden um den Konfigurator von neu zu starten.
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    Daten_Antworten.Antworten_liste.clear()

    print(Daten_Antworten.Antworten_liste)

    return render_template('frage1.html',)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
