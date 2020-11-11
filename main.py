from flask import Flask
from flask import render_template
from flask import request
import Daten_Antworten
import hunderassen

"""
Hier importieren wir die Files mit den Fragen. Die Files wurden als json geschrieben
und können daher importiert und wie Dictionaries behandelt werden.
Wenn die Files nicht richtig importiert werden können,
wird durch das Try and Except eine Fehlermeldung ausgegeben.
"""

app = Flask("Hunde Konfigurator")

antworten = Daten_Antworten.Antworten_liste


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/frage1', methods=['GET', 'POST'])
def frage1():
    if request.method == 'POST':
        antwort_frage1 = request.form['frage1']

        Daten_Antworten.antwortensichern(antwort_frage1)

    return render_template('frage1.html', frage1=frage1)


@app.route('/frage2', methods=['GET', 'POST'])
def frage2():
    if request.method == 'POST':
        antwort_frage2 = request.form['frage2']

        Daten_Antworten.antwortensichern(antwort_frage2)

    return render_template('frage2.html', frage2=frage2)


@app.route('/frage3', methods=['GET', 'POST'])
def frage3():
    if request.method == 'POST':
        antwort_frage3 = request.form['frage3']

        Daten_Antworten.antwortensichern(antwort_frage3)

    return render_template('frage3.html', frage3=frage3)


@app.route('/frage4', methods=['GET', 'POST'])
def frage4():
    if request.method == 'POST':
        antwort_frage4 = request.form['frage4']

        Daten_Antworten.antwortensichern(antwort_frage4)

    return render_template('frage4.html', frage4=frage4)


@app.route('/frage5', methods=['GET', 'POST'])
def frage5():
    if request.method == 'POST':
        antwort_frage5 = request.form['frage5']

        Daten_Antworten.antwortensichern(antwort_frage5)

    return render_template('frage5.html', frage5=frage5)


@app.route('/frage6', methods=['GET', 'POST'])
def frage6():
    if request.method == 'POST':
        antwort_frage6 = request.form['frage6']

        Daten_Antworten.antwortensichern(antwort_frage6)

    return render_template('frage6.html', frage6=frage6)



@app.route('/antwort')
def antwort():
    if antworten == hunderassen.Labrador:
        hund = 'Labrador'

    elif antworten == hunderassen.Französische_Bulldogge:
        hund = 'Französische Bulldogge'

    elif antworten == hunderassen.Chihuahua:
        hund = 'Chihuahua'

    elif antworten == hunderassen.Golden_Retriever:
        hund = 'Golden Retriever'

    elif antworten == hunderassen.Australian_Shepherd:
        hund = 'Australian_Shepherd'

    elif antworten == hunderassen.Jack_Russel:
        hund = 'Jack Russel'

    elif antworten == hunderassen.Deutscher_Schäferhund:
        hund = 'Deutscher Schäferhund'

    elif antworten == hunderassen.Havaneser:
        hund = 'Havaneser'

    elif antworten == hunderassen.Yorkshire_Terrier:
        hund = 'Yorkshire Terrier'

    elif antworten == hunderassen.Malteser:
        hund = 'Malteser'

    elif antworten == hunderassen.Border_Collie:
        hund = 'Border Collie'

    elif antworten == hunderassen.Mops:
        hund = 'Mops'

    elif antworten == hunderassen.Beagle:
        hund = 'Beagle'

    elif antworten == hunderassen.Rhodesian_Ridgeback:
        hund = 'Rhodesian Ridgeback'

    elif antworten == hunderassen.Berner_Sennenhund:
        hund = 'Berner Sennenhund'

    elif antworten == hunderassen.Dackel:
        hund = 'Dackel'

    elif antworten == hunderassen.Rottweiler:
        hund = 'Rottweiler'

    elif antworten == hunderassen.Dobermann:
        hund = 'Dobermann'

    elif antworten == hunderassen.Zwergspitz:
        hund = 'Zwergspitz'

    elif antworten == hunderassen.Boxer:
        hund = 'Zwergspitz'

    else: hund = 'Leider gibt es keinen passenden Hund für Sie. Bitte probieren Sie es erneut.'

    '''
    hund_überprüfen.hundueberpruefen()
    '''

    return render_template('antwort.html', antwort=antwort, hund=hund)


if __name__ == "__main__":
    app.run(debug=True, port=5008)