"""Webbasierte Systeme - Gruppe 07
"""
# Import benötigter Flask-Module
from flask import Flask, render_template, request, g, redirect, url_for

# Import MySQL-Connector
import mysql.connector

# Import der Verbindungsinformationen zur Datenbank:
# Variable DB_HOST: Servername des MySQL-Servers
# Variable DB_USER: Nutzername
# Variable DB_PASSWORD: Passwort
# Variable DB_DATABASE: Datenbankname
from db.db_credentials import DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE

app = Flask(__name__)


@app.before_request
def before_request():
    """ Verbindung zur Datenbank herstellen """
    g.con = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD,
                                    database=DB_DATABASE)


@app.teardown_request
def teardown_request(exception):
    """ Verbindung zur Datenbank trennen """
    con = getattr(g, 'con', None)
    if con is not None:
        con.close()


@app.route('/')
def startseite():
    """Startseite"""
    return render_template('index.html')



@app.route('/asidiropou')
def asidiropou_profil():
    cursor = g.con.cursor(dictionary=True)
    cursor.execute('SELECT * FROM asidiropou')
    daten = cursor.fetchall()
    print(daten)
    cursor.close()
    return render_template('asidiropou.html', daten=daten)


@app.route('/Bsaifo')
def bsaifo():
    cursor = g.con.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Bsaifo')
    daten = cursor.fetchall()
    print(daten)
    cursor.close()
    return render_template('Bsaifo.html', daten=daten)


@app.route('/galkudsy')
def galkudsy():
    cursor = g.con.cursor(dictionary=True)
    cursor.execute('Select id, beschreibung From galkudsy')  # sql Befehl erwarten
    daten = cursor.fetchall()
    cursor.close()
    return render_template('galkudsy.html', daten=daten)

@app.route('/alexandra')
def alexandra():
    cursor = g.con.cursor(dictionary=True)
    cursor.execute('SELECT * FROM mrosu')
    data = cursor.fetchall()
    print(data)
    cursor.close()
    return render_template('alexandra.html', data=data)


# Start der Flask-Anwendung
if __name__ == '__main__':
    app.run(debug=True)
