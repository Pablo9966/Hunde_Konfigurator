from flask import Flask
from flask import render_template
from flask import request
import daten
import Daten_Antworten

"""
Hier importieren wir die Files mit den Fragen. Die Files wurden als json geschrieben
und können daher importiert und wie Dictionaries behandelt werden.
Wenn die Files nicht richtig importiert werden können,
wird durch das Try and Except eine Fehlermeldung ausgegeben.
"""

app = Flask("Hunde Konfigurator")


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/frage1', methods=['GET', 'POST'])
def frage1():
    if request.method == 'POST':
        antwort_frage1 = request.form.getlist('frage1')

        Daten_Antworten.antwortensichern(antwort_frage1)

    return render_template('frage1.html')


@app.route('/frage2', methods=['GET', 'POST'])
def frage2():
    if request.method == 'POST':
        antwort_frage2 = request.form.getlist('frage2')

        Daten_Antworten.antwortensichern(antwort_frage2)

    return render_template('frage2.html')


@app.route('/frage3', methods=['GET', 'POST'])
def frage3():
    if request.method == 'POST':
        antwort_frage3 = request.form.getlist('frage3')

        Daten_Antworten.antwortensichern(antwort_frage3)

    return render_template('frage3.html')


@app.route('/frage4', methods=['GET', 'POST'])
def frage4():
    if request.method == 'POST':
        antwort_frage4 = request.form.getlist('frage4')

        Daten_Antworten.antwortensichern(antwort_frage4)

    return render_template('frage4.html')


@app.route('/frage5', methods=['GET', 'POST'])
def frage5():
    if request.method == 'POST':
        antwort_frage5 = request.form.getlist('frage5')

        Daten_Antworten.antwortensichern(antwort_frage5)

    return render_template('frage5.html')


@app.route('/frage6', methods=['GET', 'POST'])
def frage6():
    if request.method == 'POST':
        antwort_frage6 = request.form.getlist('frage6')

        Daten_Antworten.antwortensichern(antwort_frage6)

    return render_template('frage6.html')


@app.route('/frage7', methods=['GET', 'POST'])
def frage7():
    if request.method == 'POST':
        antwort_frage7 = request.form.getlist('frage7')

        Daten_Antworten.antwortensichern(antwort_frage7)

    return render_template('frage7.html')


if __name__ == "__main__":
    app.run(debug=True, port=5008)