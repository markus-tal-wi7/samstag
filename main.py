"""
Ziel der Demo:
Funktionierende Architektur (Frontendseite mit Daten aus Datenbank)

Markus Aufgaben vom 05.12.:
- Datenbank mit Testdaten [x]
    - User Table in Datenbank [x]
- Eine MapperKlasse: UserMapper.py [x]
    - Einige Funktionen [ ] <<<
        bspw. find_all(), find_by_name()
"""
# Für spätere Aufteilung: importiere Klassen
from src.server.bo import User
from src.server.db import Mapper
from src.server.db import UserMapper

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


import mysql.connector as connector
import os
from contextlib import AbstractContextManager
from abc import ABC, abstractmethod

