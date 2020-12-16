# zuerst importiere ich alle nötigen Funktionen und Dokumente
from flask import Flask
from flask import render_template
from flask import request
import Daten_Antworten
import hunderassen_ueberpruefen
import collections
import operator
import json
import plotly.graph_objects as px
import plotly


app = Flask("Hunde Konfigurator")


# Hier hole ich die richtigen Antworten und speichere diese schön einfach als neue liste
antworten = Daten_Antworten.Antworten_liste

# hier erstelle ich die Rangliste der Hunde. Die liste wird in im file hunderassen_ueberpruefen abgefüllt und hier wieder zurückgegeben
rangordnung = hunderassen_ueberpruefen.rangordnung_hunderassen_ueberpruefen

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

# Hier berechne ich jeweils die Anzahl Übereinstimmungen der Antworten des Users mit dem jeweiligen Hund. Dies geschieht alles im externen file hunderassen_ueberpruefen
# Labrador berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Labrador")

# Französische Bulldogge brechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Franzoesische Bulldogge")

# Chihuahua berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Chihuahua")

# Golden Retriever berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Golden Retriever")

# Australian Shepherd berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Australian Shepherd")

# Jack Russel berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Jack Russel")

# Deutscher Schäferhund berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Deutscher Schaeferhund")

# Havaneser berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Havaneser")

# Yorkshire Terrier berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Yorkshire Terrier")

# Malteser berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Malteser")

# Border Collie berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Border Collie")

# Mops berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Mops")

# Beagle berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Beagle")

# Rhodesian Ridgeback berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Rhodesian Ridgeback")

# Berner Sennenhund berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Berner Sennenhund")

# Dackel berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Dackel")

# Rottweiler Berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Rottweiler")

# Zwergspitz berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Zwergspitz")

# Boxer berechnen
    hunderassen_ueberpruefen.hunderassenueberpruefen("Boxer")


# Hier ordne ich das Dictionary antworten nach der Anzahl Übereinstimmungen
    geordnete_rangordnung = collections.OrderedDict(sorted(rangordnung.items(), key=operator.itemgetter(1), reverse=True))

# Hier hole ich die Anzahl Übereinstimmungen hervor
    anzahl_uebereinstimmungen = geordnete_rangordnung.values()

# Hier erstelle ich die Daten für die globale Rangliste. Ich speichere jeweils den Hund auf Platz 1 in einer externen liste ab. Ich muss die Liste jedoch zuerst noch in ein str umwandeln, da ich dies sonst nicht in einem .txt file abspeichern kann.
    #hier öffne ich das json file
    json_file = open("globale_rangliste.json", "r")
    data = json.load(json_file)

    #hier hole ich den platz 1 hund aufgrund der antworten des users
    erster_platz = list(geordnete_rangordnung)[:1]

    #hier wandle ich die antwort in einen string um, um mit diesem im dictionary zu suchen
    erster_platz_1 = ''.join(erster_platz)

    #hier suche ich den aktuellen aktuellen platz 1 und addiere zum wert 1 dazue, da dieser nun erneut auf platz 1 gekommen ist
    anzahl_platz_1 = data[erster_platz_1]
    neue_anzahl_platz_1 = anzahl_platz_1 +1

    #hier update ich den aktuellen platz 1 wert mit dem neuen platz 1 wert
    data[erster_platz_1] = neue_anzahl_platz_1

    #hier schreibe ich das file neu mit den aktualisierten daten
    with open("globale_rangliste.json", "w") as new_file:
        json.dump(data, new_file)

    return render_template('antwort.html', rangordnung=rangordnung, geordnete_rangordnung=geordnete_rangordnung, anzahl_uebereinstimmungen=anzahl_uebereinstimmungen, zip=zip)

#Hier soll die Antworten_Liste gelöscht werden um den Konfigurator von neu zu starten.
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    Daten_Antworten.Antworten_liste.clear()

    if request.method == 'POST':
        antwort_frage1 = request.form['frage1']

        Daten_Antworten.antwortensichern(antwort_frage1)

    return render_template('frage1.html', frage1=frage1)

#Hier wird die globale Rangliste visuell ausgegeben
@app.route('/rangliste', methods=['GET', 'GET'])
def rangliste():
    #Hier öffne ich das externe json file in dem die anzahl platz 1 aufgeliestet sind und lade das json als dictionary
    with open('globale_rangliste.json') as file:
        daten = json.load(file)

    #hier iteriere ich durch die hundenamen, damit ich nicht jeden namen manuell schreiben muss und lade diese jeweils für x und y. gleichzeitig ersetze ich "_" mit " ".
    x = []
    y = []
    for hund, punkte in daten.items():
        x.append(hund)
        y.append(punkte)

    #hier lade ich die daten ins plotty und gib es nachher aus
    fig = px.Figure(data=[px.Bar(x=x, y=y, text=y, textposition='auto'),])
    div = plotly.io.to_html(fig, include_plotlyjs=True, full_html=False)

    return render_template('rangliste.html', plotly_div=div)


if __name__ == "__main__":
    app.run(debug=True, port=5005)
