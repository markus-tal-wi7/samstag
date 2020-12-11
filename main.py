"""
Ziel der Demo:
Funktionierende Architektur (Frontendseite mit Daten aus Datenbank)

Markus Aufgaben vom 05.12.:
- Datenbank mit Testdaten [x]
    - User Table in Datenbank [x]
- Eine MapperKlasse: UserMapper.py [ ]
    - Einige Funktionen [ ]

"""
# Für spätere Aufteilung: importiere Mapper Modul
""" from server.db.Mapper import Mapper """

# Verbindung zur Datenbank ("DB") herstellen
import mysql.connector as connector
myco = connector.connect(host="127.0.0.1", user="root",
passwd="root", db="samstag", charset="utf8")

# Schnittstelle (Cursor) benennen
cursor = myco.cursor()

# Methode für SQL-Anfragen
def sql(query):
    
    try:
        cursor = myco.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        print(str(len(rows)) + " Datensätze gefunden.",
        # "Attribute: "+"Name, Salary [€]", sep=" | ",
        "")
        
        print("Attribute: ", )

        print("Lade Datensätze..." )
        
        for row in rows:
            for i in range(len(row)):
                if i == len(row)-1:
                    print((row[i]))
                else:
                    print((row[i]), end=", ")
                print("")
        
        cursor.close()

    except connector.Error as error:
        print("Failed.", error)

    finally: 
        if myco:
            myco.close()
            print()



# SQL Queries [Select by Uncomment]

# query = "select 'hello'"
query = "select * from user order by id"
# query = "select * from user order by full_name"
# query = "INSERT INTO tablename (field1, field2, field3, field4) VALUES (%s, %s, %s, %s)"
# query = ""

sql(query)


# cursor.execute(query)
# myco.commit()
# cursor.close()
# myco.close()

class 

import mysql.connector as connector
import os
from contextlib import AbstractContextManager
from abc import ABC, abstractmethod


class Mapper (AbstractContextManager, ABC):
    """Abstrakte Basisklasse aller Mapper-Klassen"""

    def __init__(self):
        self._cnx = None

    def __enter__(self):
        """Was soll geschehen, wenn wir beginnen, mit dem Mapper zu arbeiten?"""

        """Wir testen, ob der Code im Kontext der lokalen Entwicklungsumgebung oder in der Cloud ausgeführt wird.
        Dies ist erforderlich, da die Modalitäten für den Verbindungsaufbau mit der Datenbank kontextabhängig sind."""

        if True: # os.getenv('GAE_ENV', '').startswith('standard'):
            """Landen wir in diesem Zweig, so haben wir festgestellt, dass der Code in der Cloud abläuft.
            Die App befindet sich somit im **Production Mode** und zwar im *Standard Environment*.
            Hierbei handelt es sich also um die Verbindung zwischen Google App Engine und Cloud SQL."""

            """ self._cnx = connector.connect(user='demo', password='demo',
                                          unix_socket='/cloudsql/python-bankprojekt-thies:europe-west3:bank-db-thies',
                                          database='bankproject') """
            pass
        else:
            """Wenn wir hier ankommen, dann handelt sich offenbar um die Ausführung des Codes in einer lokalen Umgebung,
            also auf einem Local Development Server. Hierbei stellen wir eine einfache Verbindung zu einer lokal
            installierten mySQL-Datenbank her."""

            self._myco = myco

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Was soll geschehen, wenn wir (evtl. vorübergehend) aufhören, mit dem Mapper zu arbeiten?"""
        self._myco.close()

    """Formuliere nachfolgend sämtliche Auflagen, die instanzierbare Mapper-Subklassen mind. erfüllen müssen."""

    @abstractmethod
    def find_all(self):
        """Lies alle Tupel aus und gib sie als Objekte zurück."""
        pass

    @abstractmethod
    def find_by_key(self, key):
        """Lies den einen Tupel mit der gegebenen ID (vgl. Primärschlüssel) aus."""
        pass

    @abstractmethod
    def insert(self, object):
        """Füge das folgende Objekt als Datensatz in die DB ein."""
        pass

    @abstractmethod
    def update(self, object):
        """Ein Objekt auf einen bereits in der DB enthaltenen Datensatz abbilden."""
        pass

    @abstractmethod
    def delete(self, object):
        """Den Datensatz, der das gegebene Objekt in der DB repräsentiert löschen."""
        pass

class UserMapper:
# (Mapper)
"""Mapper-Klasse, die User-Objekte auf eine relationale
    Datenbank abbildet. Hierzu wird eine Reihe von Methoden zur Verfügung
    gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und
    gelöscht werden können. Das Mapping ist bidirektional. D.h., Objekte können
    in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    """
    def __init__(self):
            super().__init__()
    def __init__(self):
        pass
    def find_all(self):
        pass
    def find_by_name(self, name):
        pass
    def find_by_key(self, key):
        pass
    def find_by_email(self, mail_address):
        pass

"""Zu Testzwecken können wir diese Datei bei Bedarf auch ausführen, 
um die grundsätzliche Funktion zu überprüfen.

Anmerkung: Nicht professionell aber hilfreich..."""
if (__name__ == "__main__"):
    # with UserMapper() as mapper:
        result = UserMapper.find_all()
        for user in result:
            print(user)