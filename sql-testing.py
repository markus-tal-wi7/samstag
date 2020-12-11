import mysql.connector as connector
myco = connector.connect(host="127.0.0.1", user="root",
passwd="root", db="samstag", charset="utf8")
cursor = myco.cursor()

cursor = myco.cursor()
# [SELECT BY UNCOMMENTING]
query=\
"describe user"
# "select * from user order by id"
# "select 'hello'"

cursor.execute(query)
rows = cursor.fetchall()

# spalten in array auslesen
"""
columns = []
for row in rows:
    columns.append(row[0])
print(columns)
"""


for row in rows:
    for i in range(len(row)):
        if i == len(row)-1:
            print((row[i]))
        else:
            print((row[i]), end=", ")
        print("")


        
        
cursor.close()

