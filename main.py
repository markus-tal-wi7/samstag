"""
Ziel der Demo:
Einfache DB-Abfrage über Python erstellen

Markus Part:
- Datenbank mit Testdaten
    - User Table in Datenbank
- Eine MapperKlasse: UserMapper.py

"""
import mysql.connector as connector
myco = connector.connect(host="127.0.0.1", user="root",
passwd="root", db="samstag", charset="utf8")
cursor = myco.cursor()

try:
    cursor = myco.cursor()
    cursor.execute("select * from user order by full_name")
    rows = cursor.fetchall()

    print("Total rows: " + str(len(rows)),
    "Columns: "+"Name, Salary [€]",
    sep=" | ")
    print("Rows found:")
    
    for row in rows:
        print((row[0]), (row[1]), sep=", ")
    
    cursor.close()

except connector.Error as error:
    print("Failed.", error)

finally: 
    if myco:
        myco.close()
        print()

# SQL Queries [Select by Uncomment]

# query = "select 'hello'"
# query = "INSERT INTO tablename (field1, field2, field3, field4) VALUES (%s, %s, %s, %s)"
# query = ""



# cursor.execute(query)
# myco.commit()
# cursor.close()
# myco.close()

# class UserMapper (Mapper):
#     def __init__(self):
#         pass
#     def find_all(self):
#         pass
#     def find_by_name(self, name):
#         pass
#     def find_by_key(self, key):
#         pass
#     def find_by_email(self, mail_address):
#         pass