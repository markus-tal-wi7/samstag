"""
Ziel der Demo:
Funktionierende Architektur (Frontendseite mit Daten aus Datenbank)

Markus Aufgaben vom 05.12.:
- Datenbank mit Testdaten [x]
    - User Table in Datenbank [x]
- Eine MapperKlasse: UserMapper.py [ ]
    - Einige Funktionen [ ]

"""
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

class UserMapper (Mapper):
    def __init__(self):
        pass
"""     def find_all(self):
        pass
    def find_by_name(self, name):
        pass
    def find_by_key(self, key):
        pass
    def find_by_email(self, mail_address):
        pass """

"""Zu Testzwecken können wir diese Datei bei Bedarf auch ausführen, 
um die grundsätzliche Funktion zu überprüfen.

Anmerkung: Nicht professionell aber hilfreich..."""
if (__name__ == "__main__"):
    with UserMapper() as mapper:
        result = mapper.find_all()
        for user in result:
            print(user)