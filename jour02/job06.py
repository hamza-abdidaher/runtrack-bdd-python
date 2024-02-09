import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LaPlateforme"
)

mycursor = mydb.cursor()

sql_query = "SELECT SUM(capacite) FROM salle"

mycursor.execute(sql_query)

capacite_totale = mycursor.fetchone()[0]

print(f"La capacité totale des salles est de {capacite_totale}")

mycursor.close()
mydb.close()
