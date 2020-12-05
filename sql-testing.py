import mysql.connector as connector
myco = connector.connect(host="127.0.0.1", user="root",
passwd="root", db="samstag", charset="utf8")
cursor = myco.cursor()

cursor = myco.cursor()
# select query
query = "select * from user order by id"
# query = "select 'hello'"
cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    for i in range(len(row)):
        if i == len(row)-1:
            print((row[i]))
        else:
            print((row[i]), end=", ")
        print("")


        
        
cursor.close()

